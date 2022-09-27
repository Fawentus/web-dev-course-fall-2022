class Error(Exception):
    pass


class AlreadyRegisteredError(Error):
    pass


class UserNotFoundError(Error):
    pass