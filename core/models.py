import os
from typing import Union

from categories.models import Category
from courses.models import CourseFactory, AbstractCourse
from framework.errors import AlreadyExistsError, WrongCredentialsError
from users.models import UserFactory, AbstractUser

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class CustomSite:
    def __init__(self):
        self.users = []
        self.courses = []
        self.categories = []
        self.base_category = Category("base", id=0)
        with open(f"{BASE_DIR}/token.txt", "w") as f:
            f.write("")

    def create_course(self, category, course_type, name) -> Union[str, AbstractCourse]:
        return CourseFactory.create(self, category, course_type, name)

    def get_course(self, course_id: int) -> AbstractCourse:
        for item in self.courses:
            if item.id == course_id:
                return item

    def create_category(self, category_name, parent=None) -> Union[str, Category]:
        if not parent:
            parent = self.base_category
        for item in parent.children:
            if item.name == category_name:
                raise AlreadyExistsError("Category already exists")
        return Category(category_name, parent)

    def get_category(self, category_id: int = None) -> Category:
        if category_id:
            for item in self.base_category.tree():
                if item["object"].id == category_id:
                    return item["object"]

    def create_user(self, user_type: str, username, password) -> AbstractUser:
        return UserFactory.create(self, user_type, username, password)

    def get_user(self, user_id: int = None, token=None, username=None) -> AbstractUser:
        if user_id:
            for item in self.users:
                if item.id == user_id:
                    return item
        if token:
            for item in self.users:
                if item.token == token:
                    return item
        if username:
            for item in self.users:
                if item.name == username:
                    return item

    def login(self, username, password):
        user = self.get_user(username=username)
        if not user:
            raise WrongCredentialsError
        if user.password != password:
            raise WrongCredentialsError
        with open(f"{BASE_DIR}/token.txt", "w") as f:
            f.write(user.token)

    def logout(self):
        with open(f"{BASE_DIR}/token.txt", "w") as f:
            f.write("")
