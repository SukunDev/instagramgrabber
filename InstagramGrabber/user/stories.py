from typing import Optional, Dict
from InstagramGrabber import exceptions, helper, request
from InstagramGrabber.media import Media

class Stories:
    def __init__(self, user_id: int, cookies_name: Optional[str] = None):
        if not user_id:
            raise exceptions.ValueError("Error: Parameter 'user_id' not found.")
        if not cookies_name:
             raise exceptions.ValueError("Error: Parameter 'cookies_name' not found.")

        self.__cookies_name = cookies_name
        self.__user_id = user_id
       
        self.__stories_media_meta_data = None
        self._media = None
        self.__fetch_stories_media()
    
    def __fetch_stories_media(self):
        cookies = helper.load_cookies(cookies_name=self.__cookies_name)
        if cookies is None:
            raise exceptions.InstagramException('cookies not found. you need to login firts')
        response = request._excute(
                    path=f'/api/v1/feed/reels_media/?reel_ids={self.__user_id}',
                    headers={
                            "X-Csrftoken": cookies['csrftoken']
                    }, 
                    cookies=cookies
                )
        if response.status_code == 200:
             self.__stories_media_meta_data = helper.extract_json(response.text)
        else:
            raise exceptions.RequestsException((f'{response.status_code}', f'{response.reason}'))
        return self.__stories_media_meta_data

    @property
    def media(self) -> Media:
        if len(self.__stories_media_meta_data['reels']) > 1:
            return Media(self.__stories_media_meta_data['reels'][self.__user_id]["items"])
        return None