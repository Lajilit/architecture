class AlreadyExistsError(Exception):
    def __init__(self, text):
        self.text = text

class CourseTypeError(Exception):
    def __init__(self, text):
        self.text = text