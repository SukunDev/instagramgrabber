from typing import Optional
from InstagramGrabber import exceptions, helper, request
from InstagramGrabber.post.__main__ import Post
from InstagramGrabber.user.__main__ import User


class Instagram:
    def __init__(self, username: Optional[str] = None, password: Optional[str] = None):
        if not username:
            raise exceptions.ValueError("Error: Parameter 'username' not found.")
        if not password:
            raise exceptions.ValueError("Error: Parameter 'password' not found.")
        self.__username = username
        self.__password = password
    
    def login(self):
        cookies = helper.load_cookies(cookies_name=self.__username)
        if cookies is None:
            response = request._login(self.__username, self.__password)
        else:
            response = request._excute(
                    path=f'/api/v1/feed/user/{self.__username}/username/',
                    headers={
                            "X-Csrftoken": cookies['csrftoken']
                        }, 
                    cookies=cookies
                )
        if response.status_code == 200:
            res_data = helper.extract_json(response.text)
            try:
                return res_data['user']
            except KeyError:
                return res_data['logged_in_user']
        elif 'checkpoint_required' in response.text:
            res_data = helper.extract_json(response.text)
            raise exceptions.InstagramError(f'check point detected, Please Visit {res_data["checkpoint_url"]}')
        else:
            res_data = helper.extract_json(response.text)
            raise exceptions.InstagramError(res_data['message'])
    
    def get_post(self, url: Optional[str] = None) -> Post:
        if not url:
            raise exceptions.ValueError("Error: Parameter 'url' not found.")
        if "instagram.com" not in url:
            raise exceptions.ValueError(f'Invalid Instagram URL : {url}')
        if "/stories/" in url:
            raise exceptions.ValueError(f'This is stories url : {url}')
        if not helper.is_url(url):
            raise exceptions.ValueError(f'Invalid Instagram URL : {url}')
        shortcode = helper.extract_shortcode_from_url(url)
        return Post(shortcode=shortcode, cookies_name=self.__username)
    
    def get_user(self, username: Optional[str] = None) -> User:
        if not username:
            raise exceptions.ValueError("Error: Parameter 'username' not found.")
        if helper.is_url(username):
            raise exceptions.ValueError(f'Invalid Instagram Username : {username}')
        return User(username=username, cookies_name=self.__username)