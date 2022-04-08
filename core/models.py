from typing import Union

from categories.models import Category
from core.errors import AlreadyExistsError
from courses.models import CourseFactory, AbstractCourse

from users.models import UserFactory, AbstractUser


class CustomSite:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.base_category = Category("base", id=0)

    def create_user(self, user_name, user_type: str) -> AbstractUser:
        return UserFactory.create(user_name, user_type)

    def create_course(self, category, course_type, name) -> Union[str, AbstractCourse]:
        if self.get_course(category, course_type, name):
            raise AlreadyExistsError("Course already exists")
        return CourseFactory.create(category, course_type, name)

    def get_course_by_id(self, course_id: int) -> AbstractCourse:
        for item in self.courses:
            if item.id == course_id:
                return item

    def get_course(self, category, course_type, name):
        for item in self.courses:
            if (
                item.name == name
                and item.type == course_type
                and item.category == category
            ):
                return item

    def create_category(self, category_name, parent) -> Union[str, Category]:
        for item in parent.children:
            if item.name == category_name:
                raise AlreadyExistsError("Category already exists")
        return Category(category_name, parent)

    def get_category(self, category_id: int) -> Category:
        for item in self.base_category.tree():
            if item["object"].id == category_id:
                return item["object"]

    def get_user(self, user_id: int) -> Category:
        for item in self.teachers:
            if item.id == user_id:
                return item
        for item in self.students:
            if item.id == user_id:
                return item
