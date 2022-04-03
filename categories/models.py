import abc
from typing import Union

from core.errors import AlreadyExistsError


class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate(self):
        pass


class AbstractCategory(Component):
    count = 0

    def __init__(self, name: str, id=None):
        self.id = id
        self.name = name
        self._children = set()

    def check(self, category):
        for item in self._children:
            if item.name == category.name:
                raise AlreadyExistsError("Category already exists")

    def save(self):
        Category.count += 1
        self.id = self.count

    def append(self, component):
        self._children.add(component)

    def remove(self, component):
        self._children.discard(component)

    def calculate(self):
        components_count = 0
        for child in self._children:
            components_count += child.calculate()
        return components_count

    def tree(self):
        categories = [] if self.name == "base" else [{"name": self.name, "self": self}]
        for child in self._children:
            if isinstance(child, Category):
                if self.name == "base":
                    for el in child.tree():
                        categories.append(el)
                else:
                    for el in child.tree():
                        el["name"] = f"-{el['name']}"
                        categories.append(el)
        return categories


class Category(AbstractCategory):
    pass


class CategoryFactory:
    @classmethod
    def create(cls, category_name: str) -> Union[str, AbstractCategory]:
        new_category = Category(category_name)
        return new_category
