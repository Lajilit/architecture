class AlreadyExistsError(Exception):
    def __init__(self, text):
        self.text = text


class ModelTypeError(Exception):
    def __init__(self, text):
        self.text = text


class WrongCredentialsError(Exception):
    def __init__(self, text=None):
        self.text = text or "User with this login and password does not exists"


class NotExistsError(Exception):
    def __init__(self, text):
        self.text = text
