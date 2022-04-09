import copy

from categories.models import Category
from framework.errors import CourseTypeError


class CoursePrototypeMixin:
    def clone(self, category=None, course_type=None, name=None):
        clone = copy.deepcopy(self)
        if name:
            clone.name = name
        if course_type:
            clone.type = course_type
        if category:
            clone.category = category
        return clone


class AbstractCourse(CoursePrototypeMixin):
    count = 0

    def __init__(self, category: Category, name: str, type: str):
        self.id = None
        self.category = category
        self.name = name
        self.type = type

    def save(self, site):
        site.courses.append(self)
        AbstractCourse.count += 1
        self.id = self.count
        self.category.add_course(self)


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
    def create(cls, category, type, name):
        if not cls.course_types.get(type):
            raise CourseTypeError("Wrong course type")
        new_course = cls.course_types[type](category, name, type)
        return new_course
