from courses.models import CourseFactory
from framework.errors import AlreadyExistsError, CourseTypeError
from framework.response import Response
from framework.service import render_template
from framework.views import View
from settings import SITE as site

COURSE_TYPES = CourseFactory.course_types


class CourseListView(View):
    template = "courses/course_list.html"

    @staticmethod
    def get_context(request):
        context = {
            "is_authorized": request.is_authorized,
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
        except (CourseTypeError, AlreadyExistsError) as e:
            context["error"] = e.text
        else:
            new_course.save(site)
            context["success"] = "Course created"

        return Response(render_template(self.template, context=context))


class CourseCloneView(View):
    template = "courses/course_clone.html"

    @staticmethod
    def get_context(request):
        context = {
            "is_authorized": request.is_authorized,
            "title": "Clone course",
            "header": "Clone course",
            "course_types": COURSE_TYPES,
            "categories": site.base_category.tree(),
        }
        return context

    def get(self, request):
        context = self.get_context(request)
        old_course = site.get_course_by_id(
            course_id=int(request.params.get("course_id")),
        )
        context["old_course"] = old_course
        return Response(render_template(self.template, context=context))

    def post(self, request):
        context = self.get_context(request)
        old_course = site.get_course_by_id(
            course_id=int(request.data.get("old_course_id")),
        )
        context["old_course"] = old_course
        category_id = int(request.data.get("course_category"))
        category = site.get_category(category_id)
        new_course_data = {
            "category": category,
            "course_type": request.data.get("course_type"),
            "name": request.data.get("course_name"),
        }
        if site.get_course(**new_course_data):
            context["error"] = "Course already exists"
        else:
            new_course = old_course.clone(**new_course_data)
            new_course.save(site)
            context["success"] = "Course created"

        return Response(render_template(self.template, context=context))
