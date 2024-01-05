from typing import Optional, Dict
from InstagramGrabber import exceptions, request, helper
from InstagramGrabber.media import Media

class Posts:
    def __init__(self, username: Optional[str] = None, max_id: Optional[str] = None, cookies_name: Optional[str] = None):
        if not username:
            raise exceptions.ValueError("Error: Parameter 'username' not found.")
        if not cookies_name:
             raise exceptions.ValueError("Error: Parameter 'cookies_name' not found.")
        
        self.__cookies_name = cookies_name
        self.__username = username

        self.__media_meta_data = None
        self._more_available = False
        self._max_id  = None
        if max_id:
            self._max_id = max_id
        
        self._fetch_user_posts()
        
    def _fetch_user_posts(self):
        cookies = helper.load_cookies(cookies_name=self.__cookies_name)
        if cookies is None:
            raise exceptions.InstagramException('cookies not found. you need to login firts')
        url = f'/api/v1/feed/user/{self.__username}/username/?count=9'
        if self._max_id:
            url = f"{url}&max_id={self._max_id}"
        response = request._excute(
                        path=url,
                        headers={
                                "X-Csrftoken": cookies['csrftoken']
                        }, 
                        cookies=cookies
                    )
        if response.status_code == 200:
            self.__media_meta_data = helper.extract_json(response.text)
        else:
            raise exceptions.RequestsException(response.status_code, response.reason)
        
        return self.__media_meta_data
    
    @property
    def more_available(self) -> bool:
        try:
            self._more_available = self.__media_meta_data['more_available']
        except KeyError:
            self._more_available = False
        return bool(self._more_available)
    
    @more_available.setter
    def more_available(self, value):
        """Sets more_available value."""
        self._more_available = value

    @property
    def max_id(self) -> str:
        try:
            self._max_id = self.__media_meta_data['next_max_id']
        except KeyError:
            self._max_id = None
        return self._max_id
    
    @max_id.setter
    def max_id(self, value):
        """Sets max_id value."""
        self._max_id = value

    @property
    def media(self) -> Media:
        return Media(self.__media_meta_data["items"])