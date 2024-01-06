from typing import Optional
from InstagramGrabber import exceptions, helper, request
from InstagramGrabber.media import Media


class Reels:
    def __init__(self, user_id: Optional[int] = None, max_id: Optional[str] = None, cookies_name: Optional[str] = None):
        if not user_id:
            raise exceptions.ValueError("Error: Parameter 'user_id' not found.")
        if not cookies_name:
             raise exceptions.ValueError("Error: Parameter 'cookies_name' not found.")

        self.__cookies_name = cookies_name
        self.__user_id = user_id

        self.__media_meta_data = False
        self._more_available = None
        self._max_id  = None
        if max_id:
            self._max_id = max_id
        self._fetch_user_reels()

    def _fetch_user_reels(self):
        cookies = helper.load_cookies(cookies_name=self.__cookies_name)
        if cookies is None:
            raise exceptions.InstagramException('cookies not found. you need to login firts')
        data = {
                "include_feed_video": True,
                "page_size": 9,
                "target_user_id": self.__user_id
        }
        if self._max_id:
            data.update({"max_id": self._max_id})
        response = request._excute(
                        path=f'/api/v1/clips/user/',
                        data=data,
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
            self._more_available = self.__media_meta_data['paging_info']['more_available']
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
            self._max_id = self.__media_meta_data['paging_info']['max_id']
        except KeyError:
            self._max_id = None
        return self._max_id
    
    @max_id.setter
    def max_id(self, value):
        """Sets max_id value."""
        self._max_id = value

    @property
    def media(self) -> Media:
        if len(self.__media_meta_data["items"]) > 1:
            return Media(self.__media_meta_data["items"])
        return None