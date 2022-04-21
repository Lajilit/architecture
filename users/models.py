from framework.errors import AlreadyExistsError, ModelTypeError


class AbstractUser:
    count = 0

    def __init__(self, name: str, password: str):
        self.id = None
        self.name = name
        self.password = password
        self.token = f"{self.name}{self.password}"

    def save(self, site):
        AbstractUser.count += 1
        self.id = self.count
        site.users.append(self)


class Teacher(AbstractUser):
    user_type = "teacher"


class Student(AbstractUser):
    user_type = "student"


class UserFactory:
    user_models = {"student": Student, "teacher": Teacher}

    @classmethod
    def create(cls, site, user_type, username, password):
        user_model = cls.user_models.get(user_type)

        if not user_model:
            raise ModelTypeError("Wrong user type")

        if cls.check_user_exists(site, user_model, username):
            raise AlreadyExistsError(
                f"{user_type.title()} with username {username} already exists"
            )

        new_user = user_model(username, password)
        return new_user

    @staticmethod
    def check_user_exists(site, user_model, username):
        for item in site.users:
            if item.name == username and isinstance(item, user_model):
                return True
