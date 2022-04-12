import abc


class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate(self):
        pass


class Category(Component):
    count = 0

    def __init__(self, name: str, parent: "Category" = None, id=None):
        self.id = id
        self.name = name
        self.parent = parent
        self.children = set()
        self.courses = set()

    def save(self, site):
        site.categories.append(self)
        Category.count += 1
        self.id = self.count
        self.parent.add_child(self)

    def add_child(self, component):
        self.children.add(component)

    def remove_child(self, component):
        self.children.discard(component)

    def add_course(self, course):
        self.courses.add(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def calculate(self):
        courses_count = len(self.courses)
        for child in self.children:
            courses_count += child.calculate()
        return courses_count

    def tree(self):
        categories_tree = (
            [] if self.name == "base" else [{"name": self.name, "object": self}]
        )
        for child in self.children:
            if self.name == "base":
                for el in child.tree():
                    categories_tree.append(el)
            else:
                for el in child.tree():
                    el["name"] = f"-{el['name']}"
                    categories_tree.append(el)
        return categories_tree
