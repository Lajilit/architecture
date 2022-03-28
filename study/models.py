import copy


class AbstractUser:
    pass


class Teacher(AbstractUser):
    pass


class Student(AbstractUser):
    pass


class UserFactory:
    types = {"student": Student, "teacher": Teacher}

    @classmethod
    def create(cls, user_type: str):
        return cls.types[user_type]()


class CoursePrototypeMixin:
    def clone(self, name=None, type=None):
        clone = copy.deepcopy(self)
        if name:
            clone.name = name
        if type:
            clone.type = type
        return clone


class AbstractCourse(CoursePrototypeMixin):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        self.clone_url = (
            f"/clone_course/?course_name={self.name}&course_type={self.type}"
        )


class InteractiveCourse(AbstractCourse):
    pass


class VebinarCourse(AbstractCourse):
    pass


class RecordedCourse(AbstractCourse):
    pass


class CourseFactory:
    course_types = {
        "interactive": InteractiveCourse,
        "vebinar": VebinarCourse,
        "recorded": RecordedCourse,
    }

    @classmethod
    def create(cls, course_type, course_name):
        if cls.course_types.get(course_type):
            return cls.course_types[course_type](course_name, course_type)


class CustomSite:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []

    def create_user(self, user_type: str):
        return UserFactory.create(user_type)

    def create_course(self, course_type, course_name):
        return CourseFactory.create(course_type, course_name)

    def get_course(self, course_name, course_type) -> AbstractCourse:
        for item in self.courses:
            if item.name == course_name and item.type == course_type:
                return item
