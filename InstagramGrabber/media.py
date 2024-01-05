from typing import Optional, Dict
from InstagramGrabber import exceptions, helper
import json

class Media:
    def __init__(self, media_meta_data: Optional[Dict] = None):
        if not media_meta_data:
            raise exceptions.ValueError(f"Error: Parameter 'media_meta_data' not found.")
        self.__media_meta_data = helper.extract_all_media(media_meta_data)

    def __len__(self):
        return len(self.__media_meta_data)

    def __getitem__(self, key):
        return self.__media_meta_data[key]
    
    def __repr__(self) -> str:
        return repr(self.__media_meta_data)

    def prettify(self, indent: Optional[int] = 2):
        return json.dumps(self, cls=MediaEncoder, indent=indent)

class MediaEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Media):
            return obj._Media__media_meta_data
        return super().default(obj)