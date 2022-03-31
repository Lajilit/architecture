import copy
from categories.models import AbstractCategory
from core.errors import AlreadyExistsError, CourseTypeError


class CoursePrototypeMixin:
    def clone(self, category=None, type=None, name=None):
        clone = copy.deepcopy(self)
        if name:
            clone.name = name
        if type:
            clone.type = type
        if category:
            clone.category = category
        return clone


class AbstractCourse(CoursePrototypeMixin):
    count = 0

    def __init__(self, site, category: AbstractCategory, name: str, type: str):
        self.id = None
        self.category = category
        self.name = name
        self.type = type

    def check(self, site):
        for item in site.courses:
            if item.name == self.name \
                    and item.type == self.type \
                    and item.category == self.category:
                raise AlreadyExistsError("Course already exists")

    def save(self, site):
        site.courses.append(self)
        AbstractCourse.count += 1
        self.id = self.count


class InteractiveCourse(AbstractCourse):
    pass


class VebinarCourse(AbstractCourse):
    pass


class CourseFactory:
    course_types = {
        "online": InteractiveCourse,
        "offline": VebinarCourse,
    }

    @classmethod
    def create(cls, site, category, type, name):
        if not cls.course_types.get(type):
            raise CourseTypeError("Wrong course type")
        new_course = cls.course_types[type](
            site, category, name, type
        )
        return new_course
