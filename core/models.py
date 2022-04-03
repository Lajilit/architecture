from typing import Union

from categories.models import AbstractCategory, CategoryFactory
from courses.models import CourseFactory, AbstractCourse

from users.models import UserFactory, AbstractUser


class CustomSite:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []

    def create_user(self, user_name, user_type: str) -> AbstractUser:
        return UserFactory.create(user_name, user_type)

    def create_course(self, category, type, name) -> Union[str, AbstractCourse]:
        return CourseFactory.create(category, type, name)

    def create_category(self, category_name) -> Union[str, AbstractCategory]:
        return CategoryFactory.create(category_name)

    def get_course(self, course_id: int) -> AbstractCourse:
        for item in self.courses:
            if item.id == course_id:
                return item

    def get_category(self, category_id: int) -> AbstractCategory:
        for item in self.categories:
            if item.id == category_id:
                return item

    def get_user(self, user_id: int) -> AbstractCategory:
        for item in self.teachers:
            if item.id == user_id:
                return item
        for item in self.students:
            if item.id == user_id:
                return item
