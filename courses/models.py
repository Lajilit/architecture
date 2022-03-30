import copy



class CoursePrototypeMixin:
    def clone(self, type=None, name=None):
        clone = copy.deepcopy(self)
        if name:
            clone.name = name
        if type:
            clone.type = type
        clone.clone_url = (
            f"/clone_course/?course_name={clone.name}&course_type={clone.type}"
        )
        return clone


class AbstractCourse(CoursePrototypeMixin):
    count = 0

    def __init__(self, site, name: str, type: str):
        self.id = None
        self.name = name
        self.type = type
        self.site = site

    def save(self):
        self.site.courses.append(self)
        AbstractCourse.count += 1
        self.id = self.count


class InteractiveCourse(AbstractCourse):
    pass


class VebinarCourse(AbstractCourse):
    pass


class CourseFactory:
    course_types = {
        "online": InteractiveCourse,
        "offline": VebinarCourse,
    }

    @classmethod
    def create(cls, site, course_type, course_name):
        if cls.course_types.get(course_type):
            return cls.course_types[course_type](site, course_name, course_type)
