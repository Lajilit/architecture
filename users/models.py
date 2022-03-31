from typing import Union

from core.errors import AlreadyExistsError


class AbstractUser:
    count = 0

    def __init__(self, site, name: str):
        self.id = None
        self.name = name

    def save(self, site):
        AbstractUser.count += 1
        self.id = self.count


class Teacher(AbstractUser):
    def __init__(self, site, name):
        super().__init__(site, name)
        for item in site.teachers:
            if item.name == name:
                raise AlreadyExistsError("Teacher already exists")

    def save(self, site):
        super().save(site)
        site.teachers.append(self)


class Student(AbstractUser):
    def __init__(self, site, name):
        super().__init__(site, name)
        for item in site.students:
            if item.name == name:
                raise AlreadyExistsError("Student already exists")

    def save(self, site):
        super().save(site)
        site.students.append(self)


class UserFactory:
    types = {"student": Student, "teacher": Teacher}

    @classmethod
    def create(cls, site, user_name, user_type: str) -> Union[str, AbstractUser]:
        try:
            new_user = cls.types[user_type](site, user_name)
        except AlreadyExistsError as e:
            return e.text
        return new_user
