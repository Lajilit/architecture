from typing import Union

from core.errors import AlreadyExistsError


class AbstractUser:
    count = 0

    def __init__(self, name: str):
        self.id = None
        self.name = name

    def save(self, site):
        AbstractUser.count += 1
        self.id = self.count


class Teacher(AbstractUser):
    def __init__(self, name):
        super().__init__(name)

    def save(self, site):
        super().save(site)
        site.teachers.append(self)


class Student(AbstractUser):
    def __init__(self, name):
        super().__init__(name)

    def save(self, site):
        super().save(site)
        site.students.append(self)


class UserFactory:
    types = {"student": Student, "teacher": Teacher}

    @classmethod
    def create(cls, user_name, user_type: str) -> Union[str, AbstractUser]:
        try:
            new_user = cls.types[user_type](user_name)
        except AlreadyExistsError as e:
            return e.text
        return new_user
