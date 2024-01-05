from typing import Optional
from InstagramGrabber import exceptions, request, helper
from InstagramGrabber.user.posts import Posts
from InstagramGrabber.user.reels import Reels
from InstagramGrabber.user.stories import Stories

class User:
    def __init__(self, username: Optional[str] = None, user_meta_data: Optional[str] = None, cookies_name: Optional[str] = None):
        if not username:
            raise exceptions.ValueError("Error: Parameter 'username' not found.")
        
        if not cookies_name:
             raise exceptions.ValueError("Error: Parameter 'cookies_name' not found.")
        
        self.__cookies_name = cookies_name
        
        if user_meta_data:
            self.__user_meta_data = user_meta_data
        else:
            self.__user_meta_data = self._fetch_user_by_username(username=username, cookies_name=self.__cookies_name)

        self.__media_meta_data= None

        self._username = username
        self._full_name = None
        self._biography = None
        self._category_name = None
        self._following = None
        self._followers = None
        self._posts_count = None
        self._profile_picture = None
        self._user_id = None
        self._is_private = None
        self._is_verified = None

    
    def get_post(self, max_id: Optional[str] = None) -> Posts:
        return Posts(username=self._username, cookies_name=self.__cookies_name, max_id=max_id)
    
    def get_reel(self, max_id: Optional[str] = None) -> Reels:
        return Reels(user_id=self.user_id, cookies_name=self.__cookies_name, max_id=max_id)
    
    def get_stories(self) -> Stories:
        return Stories(user_id=self.user_id, cookies_name=self.__cookies_name)
    
    @staticmethod
    def _fetch_user_by_username(username, cookies_name):
        cookies = helper.load_cookies(cookies_name=cookies_name)
        if cookies is None:
            raise exceptions.InstagramException('cookies not found. you need to login firts')
        response = request._excute(
                path=f'/api/v1/users/web_profile_info/?username={username}',
                headers={
                                "X-Csrftoken": cookies['csrftoken']
                }, 
                cookies=cookies
        )
        if response.status_code == 200:
            user_meta_data = helper.extract_json(response.text)["data"]["user"]
        else:
            raise exceptions.RequestsException((f'{response.status_code}', f'{response.reason}'))
            
        return user_meta_data


    @property
    def username(self):
        if self._username:
            return self._username
        try:
            self._username = self.__user_meta_data["username"]
        except KeyError:
            raise exceptions.InstagramException( f'Exception while accessing username of {self._username}.')  
        return self._username

    @username.setter
    def username(self, value):
        """Sets the username value."""
        self._username = value

    @property
    def full_name(self):
        if self._full_name:
            return self._full_name
        try:
            self._full_name = self.__user_meta_data["full_name"]
        except KeyError:
            raise exceptions.InstagramException( f'Exception while accessing full_name of {self._username}. ')  
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        """Sets the full_name value."""
        self._full_name = value

    @property
    def biography(self):
        if self._biography:
            return self._biography
        try:
            self._biography = self.__user_meta_data["biography"]
        except KeyError:
            raise exceptions.InstagramException( f'Exception while accessing biography of {self._username}. ')  
        return self._biography

    @biography.setter
    def biography(self, value):
        """Sets the biography value."""
        self._biography = value

    @property
    def category_name(self):
        if self._category_name:
            return self._category_name
        try:
            self._category_name = self.__user_meta_data["category_name"]
        except KeyError:
            raise exceptions.InstagramException( f'Exception while accessing category_name of {self._username}. ')  
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        """Sets the category_name value."""
        self._category_name = value

    @property
    def following(self):
        if self._following:
            return self._following
        try:
            self._following = self.__user_meta_data["edge_follow"]["count"]
        except KeyError:
            raise exceptions.InstagramException( f'Exception while accessing following of {self._username}. ')  
        return self._following
    
    @following.setter
    def following(self, value):
        """Sets the following value."""
        self._following = value

    @property
    def followers(self):
        if self._followers:
            return self._followers
        try:
            self._followers = self.__user_meta_data["edge_followed_by"]["count"]
        except KeyError:
            raise exceptions.InstagramException( f'Exception while accessing followers of {self._username}. ')  
        return self._followers

    @followers.setter
    def followers(self, value):
        """Sets the followers value."""
        self._followers = value

    @property
    def posts_count(self):
        if self._posts_count:
            return self._posts_count
        try:
            self._posts_count = self.__user_meta_data["edge_owner_to_timeline_media"]["count"]
        except KeyError:
            raise exceptions.InstagramException( f'Exception while accessing posts_count of {self._username}. ')  
        return self._posts_count

    @posts_count.setter
    def posts_count(self, value):
        """Sets the posts_count value."""
        self._posts_count = value

    @property
    def profile_picture(self):
        if self._profile_picture:
            return self._profile_picture
        try:
            self._profile_picture = self.__user_meta_data["profile_pic_url_hd"]
        except KeyError:
            raise exceptions.InstagramException( f'Exception while accessing profile_picture of {self._username}. ')  
        return self._profile_picture

    @profile_picture.setter
    def profile_picture(self, value):
        """Sets the profile_picture value."""
        self._profile_picture = value

    @property
    def user_id(self):
        if self._user_id:
            return self._user_id
        try:
            self._user_id = self.__user_meta_data["id"]
        except KeyError:
            raise exceptions.InstagramException( f'Exception while accessing user_id of {self._username}. ')  
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Sets the user_id value."""
        self._user_id = value

    @property
    def is_private(self):
        if self._is_private:
            return self._is_private
        try:
            self._is_private = self.__user_meta_data["is_private"]
        except KeyError:
            raise exceptions.InstagramException( f'Exception while accessing is_private of {self._username}. ')  
        return self._is_private

    @is_private.setter
    def is_private(self, value):
        """Sets the is_private value."""
        self._is_private = value

    @property
    def is_verified(self):
        if self._is_verified:
            return self._is_verified
        try:
            self._is_verified = self.__user_meta_data["is_verified"]
        except KeyError:
            raise exceptions.InstagramException( f'Exception while accessing is_verified of {self._username}. ')  
        return self._is_verified

    @is_verified.setter
    def is_verified(self, value):
        """Sets the is_verified value."""
        self._is_verified = value