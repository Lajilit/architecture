from typing import Union

from core.errors import AlreadyExistsError


class AbstractCategory:
    count = 0

    def __init__(self, site, name: str):
        self.id = None
        self.name = name

    def check(self, site):
        for item in site.categories:
            if item.name == self.name:
                raise AlreadyExistsError("Category already exists")

    def save(self, site):
        site.categories.append(self)
        Category.count += 1
        self.id = self.count


class Category(AbstractCategory):
    pass


class CategoryFactory:
    @classmethod
    def create(cls, site, category_name: str) -> Union[str, AbstractCategory]:
        new_category = Category(site, category_name)
        return new_category
