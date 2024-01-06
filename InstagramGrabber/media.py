from typing import Any, Optional, Dict
from InstagramGrabber import exceptions, helper
import json

class Media:
    def __init__(self, media_meta_data: Optional[Dict] = None):
        if not media_meta_data:
            raise exceptions.ValueError(f"Error: Parameter 'media_meta_data' not found.")
        self.__media_meta_data = helper.extract_all_media(media_meta_data)

    @property
    def json(self):
        return self.__media_meta_data.copy()

    def prettify(self, indent: Optional[int] = None):
        return json.dumps(self.__media_meta_data, indent=indent)

    def __len__(self):
        return len(self.__media_meta_data)

    def __getitem__(self, key):
        return self.__media_meta_data[key]
    
    def __repr__(self) -> str:
        return repr(self.__media_meta_data)