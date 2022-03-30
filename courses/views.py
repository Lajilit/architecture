from settings import SITE as site
from courses.models import CourseFactory
from framework.response import Response
from framework.service import render_template
from framework.views import View

COURSE_TYPES = CourseFactory.course_types


class CourseListView(View):
    @staticmethod
    def get(request):
        context = {
            "is_authorized": request.is_authorized,
            "title": "Course categories",
            "header": "Course categories",
        }
        return Response(render_template("users/categories_list.html", context=context))


class CourseCreateView(View):
    def get(self, request):
        template = "users/category_create.html"
        context = {
            "is_authorized": request.is_authorized,
            "title": "Create users",
            "header": "Create users",
            'course_types': COURSE_TYPES
        }
        if request.path == "/clone_course/":
            template = "users/course_clone.html"
            params = request.params
            course_to_clone = site.get_course(
                course_id=params.get("course_id")[0],
            )
            context["title"] = "Clone users"
            context["header"] = "Clone users"
            context["old_course"] = course_to_clone
        return Response(render_template(template, context=context))

    def post(self, request):
        template = "users/category_create.html"
        context = {
            "is_authorized": request.is_authorized,
            "title": "Create users",
            "header": "Create users",
            'course_types': COURSE_TYPES
        }
        data = request.data
        new_course = site.create_course(
            course_type=data.get("course_type")[0],
            course_name=data.get("course_name")[0],
        )
        if request.path == "/clone_course/":
            course_to_clone = site.get_course(
                course_id=data.get("old_course_id")[0],
            )
            new_course = course_to_clone.clone(
                type=data.get("course_type")[0],
                name=data.get("course_name")[0]
            )
            template = "users/course_clone.html"
            context["title"] = "Clone users"
            context["header"] = "Clone users"
            context["old_course"] = course_to_clone

        if site.check_course_exists(new_course.name, new_course.type):
            context["error"] = "users already exists"
        elif not new_course:
            context["error"] = "wrong course_type"
        else:
            new_course.save(site)
            template = "users/success.html"
            context = {
                "is_authorized": request.is_authorized,
                "title": "Course created",
                "header": "Course created",
                "users": new_course,
            }

        return Response(render_template(template, context=context))
