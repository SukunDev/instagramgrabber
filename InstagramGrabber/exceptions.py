class InstagramException(Exception):
    """Error handling Untuk Module Instagram"""

class ValueError(InstagramException):
    """Value Error Handling"""

class RequestsException(InstagramException):
    """Error handling Untuk Module Requests"""