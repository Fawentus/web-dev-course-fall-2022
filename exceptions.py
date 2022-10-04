class UserAlreadyRegisteredError(Exception):
    def __init__(self):
        Exception.__init__(self, "You are already registered")


class NameAlreadyRegisteredError(Exception):
    def __init__(self):
        Exception.__init__(self, "Choose another name")

class UserNotRegisteredError(Exception):
    def __init__(self):
        Exception.__init__(self, "First you have to register!")