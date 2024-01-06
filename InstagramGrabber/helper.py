import pickle
import base64
import json
import os
import re
from urllib.parse import urlparse, unquote, urlunparse
from InstagramGrabber import exceptions
from typing import Any, Dict

def save_cookies(cookies, cookies_name) -> None:
    if not os.path.exists(f'./instagram_cookies/'):
        os.makedirs(f'./instagram_cookies/')
    with open(f'./instagram_cookies/{cookies_name}_cookies', 'wb') as f:
        pickle.dump(cookies, f)

def load_cookies(cookies_name) -> Any:
    try:
        if not os.path.exists(f'./instagram_cookies/'):
            os.makedirs(f'./instagram_cookies/')
        with open(f'./instagram_cookies/{cookies_name}_cookies', 'rb') as f:
            cookies = pickle.load(f)
    except Exception as e:
        cookies = None
    return cookies

def extract_shortcode_from_url(url) -> str:
    remove_query_and_trailing_slash = lambda url: urlunparse(urlparse(url)._replace(query="")._replace(path=urlparse(url).path.rstrip("/")))
    parsed_url = urlparse(remove_query_and_trailing_slash(url))
    path_segments = parsed_url.path.split('/')
    if len(path_segments) <= 2:
        raise exceptions.InstagramError(f'can\'t find shortcode')
    return path_segments[2]
    
def extract_username_from_url(url) -> str:
    remove_query_and_trailing_slash = lambda url: urlunparse(urlparse(url)._replace(query="")._replace(path=urlparse(url).path.rstrip("/")))
    parsed_url = urlparse(remove_query_and_trailing_slash(url))
    path_segments = parsed_url.path.split('/')
    if len(path_segments) <= 1:
        raise exceptions.InstagramError(f'invalid instagram URL {url}')
    
    return path_segments[1]

def instagram_shortcode_to_media_id(code) -> int:
    if len(code) > 11:
        return None
    code = 'A' * (12 - len(code)) + code
    return int.from_bytes(base64.b64decode(code.encode(), b'-_'), 'big')

def get_best_quality(data) -> Dict:
    best_image = max(data, key=lambda x: x["width"] * x["height"])
    return {
        "width": best_image['width'],
        "height": best_image['height'],
        "url": best_image['url'],
    }

def extract_json(data) -> Dict:
    return json.loads(data)

def is_url(url) -> bool:
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def extract_all_media(items) -> Dict:
    all_media = []
    for item in items:
        media = None
        try:
            media = item["media"]
        except KeyError:
            media = item
        media_id = media['pk']
        shortcode = media['code']
        product_type = media["product_type"]
        captions = None
        if media["caption"] is not None and media["caption"]["text"] is not None:
            captions = media["caption"]["text"]
        result = {
            "media_id": media_id,
            "shortcode": shortcode,
            "product_type": product_type,
            "caption": captions,
        }
        if product_type == "feed":
            choose_media = get_best_quality(media["image_versions2"]["candidates"])
            choose_media.update({"type": "image"})
            if "id" in choose_media:
                choose_media.pop("id")
            result.update({
                "media": choose_media
            })
        elif product_type == "clips":
            choose_media = get_best_quality(media["video_versions"])
            choose_media.update({"type": "video"})
            if "id" in choose_media:
                choose_media.pop("id")
            result.update({
                "media": choose_media
            })
        elif product_type == "story":
            try:
                choose_media = get_best_quality(media["video_versions"])
                choose_media.update({"type": "video"})
            except KeyError:
                choose_media = get_best_quality(media["image_versions2"]["candidates"])
                choose_media.update({"type": "image"})
            if "id" in choose_media:
                choose_media.pop("id")
            result.update({
                "media": choose_media
            })
        elif product_type == "carousel_container":
            carousel_media = []
            for carousel in media["carousel_media"]:
                try:
                    choose_media = get_best_quality(carousel["video_versions"])
                    choose_media.update({"type": "video"})
                except KeyError:
                    choose_media = get_best_quality(carousel["image_versions2"]["candidates"])
                    choose_media.update({"type": "image"})
                carousel_media.append({
                    "media_id": carousel["pk"],
                    "product_type": carousel["product_type"],
                    "media": choose_media,
                })
            result.update({
                "carousel_media": carousel_media
            })
        else:
            try:
                choose_media = get_best_quality(media["video_versions"])
                choose_media.update({"type": "video"})
            except KeyError:
                choose_media = get_best_quality(media["image_versions2"]["candidates"])
                choose_media.update({"type": "image"})
            result.update({
                "media": choose_media
            })
        all_media.append(result)
    return all_media