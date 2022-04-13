import copy

from categories.models import Category
from framework.errors import ModelTypeError, AlreadyExistsError


class CoursePrototypeMixin:
    def clone(self, category=None, name=None):
        clone = copy.deepcopy(self)
        if name:
            clone.name = name
        if category:
            clone.category = category
        return clone


class AbstractCourse(CoursePrototypeMixin):
    count = 0
    course_type = None

    def __init__(self, category: Category, name: str):
        self.id = None
        self.category = category
        self.name = name
        self.students = []
        self.teacher = None

    def save(self, site):
        site.courses.append(self)
        AbstractCourse.count += 1
        self.id = self.count
        self.category.add_course(self)


class InteractiveCourse(AbstractCourse):
    course_type = "online"
    pass


class VebinarCourse(AbstractCourse):
    course_type = "offline"
    pass


class CourseFactory:
    course_models = {
        "online": InteractiveCourse,
        "offline": VebinarCourse,
    }

    @classmethod
    def create(cls, site, category, course_type, name):
        course_model = cls.course_models.get(course_type)

        if not course_model:
            raise ModelTypeError("Wrong course type")

        if cls.check_course_exists(site, course_model, category, name):
            raise AlreadyExistsError("Course already exists")

        new_course = course_model(category, name)
        return new_course

    @staticmethod
    def check_course_exists(site, course_model, category, name):
        for item in site.courses:
            if (
                item.name == name
                and item.category == category
                and isinstance(item, course_model)
            ):
                return True
