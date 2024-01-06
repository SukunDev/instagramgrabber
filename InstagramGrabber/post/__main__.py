from typing import Optional
from InstagramGrabber import exceptions, helper, request
from InstagramGrabber.user.__main__ import User
from InstagramGrabber.media import Media

class Post:
    def __init__(self, shortcode: Optional[str] = None, cookies_name: Optional[str] = None):
        if not shortcode:
            raise exceptions.ValueError("Error: Parameter 'shortcode' not found.")
        if not cookies_name:
             raise exceptions.ValueError("Error: Parameter 'cookies_name' not found.")
        self.__cookies_name = cookies_name
        self.__shortcode = shortcode
        
        self._media_id = helper.instagram_shortcode_to_media_id(self.__shortcode)
        if not self._media_id:
             raise exceptions.InstagramException(f'can\'t extract media id from shortcode {self.__shortcode}')
        
        self.__media_meta_data = None
        self.__fetch_media()

        self.__username = self.__media_meta_data["items"][0]['user']["username"]
        self.__user = User._fetch_user_by_username(username=self.__username, cookies_name=self.__cookies_name)
        
    def __fetch_media(self):
        cookies = helper.load_cookies(cookies_name=self.__cookies_name)
        if cookies is None:
                raise exceptions.InstagramException('cookies not found. you need to login firts')
        response = request._excute(
                        path=f'/api/v1/media/{self._media_id}/info/',
                        headers={
                                "X-Csrftoken": cookies['csrftoken']
                        }, 
                        cookies=cookies
                    )
        if response.status_code == 200:
            self.__media_meta_data = helper.extract_json(response.text)
        elif "Media not found or unavailable" in response.text:
            raise exceptions.InstagramException('Media not found or unavailable')
        else:
            raise exceptions.RequestsException((f'{response.status_code}', f'{response.reason}'))
        return self.__media_meta_data
    
    @property
    def media(self) -> Media:
        if len(self.__media_meta_data["items"]) > 1:
                return Media(self.__media_meta_data["items"])
        return None

    @property
    def user(self) -> User:
        return User(username=self.__username, user_meta_data=self.__user, cookies_name=self.__cookies_name)