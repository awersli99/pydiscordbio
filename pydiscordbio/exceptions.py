class APIError(Exception):
    """Raised when there is an API error"""
    pass


class NotFound(Exception):
    """Raised on a 404 status code"""
    pass


class UserNotFound(Exception):
    """Raised when a specified user cannot be found by the API"""
    pass


class InvalidSearch(Exception):
    """Raised when a search query is invalid"""
    pass
