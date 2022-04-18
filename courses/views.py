from courses.models import CourseFactory
from framework.errors import AlreadyExistsError, ModelTypeError
from framework.response import Response
from framework.service import render_template
from framework.views import View
from settings import SITE as site

COURSE_TYPES = CourseFactory.course_models


class CourseListView(View):
    template = "courses/course_list.html"

    @staticmethod
    def get_context(request):
        context = {
            "is_authorized": request.is_authorized,
            "user": request.user,
            "title": "Courses",
            "header": "Courses",
            "objects": site.courses,
        }
        return context

    def get(self, request):
        context = self.get_context(request)
        context["categories"] = site.base_category.tree()
        return Response(render_template(self.template, context=context))


class CourseCreateView(View):
    template = "courses/course_create.html"

    @staticmethod
    def get_context(request):
        context = {
            "is_authorized": request.is_authorized,
            "user": request.user,
            "title": "Create course",
            "header": "Create course",
            "course_types": COURSE_TYPES,
            "categories": site.base_category.tree(),
        }
        return context

    def get(self, request):
        context = self.get_context(request)
        return Response(render_template(self.template, context=context))

    def post(self, request):
        context = self.get_context(request)

        category_id = int(request.data.get("course_category"))
        category = site.get_category(category_id)
        new_course_data = {
            "category": category,
            "course_type": request.data.get("course_type"),
            "name": request.data.get("course_name"),
        }
        try:
            new_course = site.create_course(**new_course_data)
        except (ModelTypeError, AlreadyExistsError) as e:
            context["error"] = e.text
        else:
            new_course.save(site)
            context["success"] = f"{new_course.course_type.title()} course created"

        return Response(render_template(self.template, context=context))


class CourseCloneView(View):
    template = "courses/course_clone.html"

    @staticmethod
    def get_context(request):
        context = {
            "is_authorized": request.is_authorized,
            "user": request.user,
            "title": "Clone course",
            "header": "Clone course",
            "course_types": COURSE_TYPES,
            "categories": site.base_category.tree(),
        }
        return context

    def get(self, request):
        context = self.get_context(request)
        old_course = site.get_course(
            course_id=int(request.params.get("course_id")),
        )
        context["old_course"] = old_course
        return Response(render_template(self.template, context=context))

    def post(self, request):
        context = self.get_context(request)
        old_course = site.get_course(
            course_id=int(request.data.get("old_course_id")),
        )
        course_model = type(old_course)
        context["old_course"] = old_course
        category_id = int(request.data.get("course_category"))
        category = site.get_category(category_id)
        new_course_data = {
            "category": category,
            "name": request.data.get("course_name"),
        }
        if CourseFactory.check_course_exists(site, course_model, **new_course_data):
            context["error"] = "Course already exists"
        else:
            new_course = old_course.clone(**new_course_data)
            new_course.save(site)
            context["success"] = f"{new_course.course_type.title()} course cloned"

        return Response(render_template(self.template, context=context))


class CourseRetrieveView(View):
    template = "courses/course_retrieve.html"

    @staticmethod
    def get_context(request):
        context = {
            "is_authorized": request.is_authorized,
            "user": request.user,
        }
        return context

    def get(self, request):
        context = self.get_context(request)
        course_id = int(request.params.get("course_id"))
        course = site.get_course(course_id)
        context.update(
            {
                "title": f"Course {course.name} ({course.course_type})",
                "header": f"Course {course.name} ({course.course_type})",
                "course": course,
            }
        )
        return Response(render_template(self.template, context=context))

    def post(self, request):
        context = self.get_context(request)

        course_id = int(request.params.get("course_id"))
        course = site.get_course(course_id)
        context.update(
            {
                "title": f"Course {course.name} ({course.course_type})",
                "header": f"Course {course.name} ({course.course_type})",
                "course": course,
            }
        )
        try:
            course.add_user(request.user)
        except AlreadyExistsError as e:
            context["error"] = e.text
        else:
            context["success"] = f"You added course {course.course_type.title()}"

        return Response(render_template(self.template, context=context))
