from core.errors import AlreadyExistsError, CourseTypeError
from courses.models import CourseFactory
from framework.response import Response
from framework.service import render_template
from framework.views import View
from settings import SITE as site

COURSE_TYPES = CourseFactory.course_types


class CourseListView(View):
    @staticmethod
    def get(request):
        context = {
            "is_authorized": request.is_authorized,
            "title": "Courses",
            "header": "Courses",
            "courses": site.courses
        }
        return Response(render_template("courses/course_list.html", context=context))


class CourseCreateView(View):
    def get(self, request):
        categories = site.categories
        template = "courses/course_create.html"
        context = {
            "is_authorized": request.is_authorized,
            "title": "Create course",
            "header": "Create course",
            'course_types': COURSE_TYPES,
            "categories": categories
        }
        if request.path == "/courses/clone":
            template = "courses/course_clone.html"
            params = request.params
            course_to_clone = site.get_course(
                course_id=int(params.get("course_id")[0]),
            )
            print(course_to_clone.name)
            context["title"] = "Clone users"
            context["header"] = "Clone users"
            context["old_course"] = course_to_clone
        return Response(render_template(template, context=context))

    def post(self, request):
        template = "courses/course_create.html"
        categories = site.categories
        context = {
            "is_authorized": request.is_authorized,
            "title": "Create course",
            "header": "Create course",
            'course_types': COURSE_TYPES,
            "categories": categories
        }
        new_course = None
        category_id = int(request.data.get("course_category")[0])
        category = site.get_category(category_id)
        new_course_data = {
            "category": category,
            "type": request.data.get("course_type")[0],
            "name": request.data.get("course_name")[0],
        }
        print(new_course_data)
        if request.path == "/courses/clone":
            template = "courses/course_clone.html"
            context["title"] = context["header"] = "Clone course"
            course_to_clone = site.get_course(
                course_id=int(request.data.get("old_course_id")[0]),
            )

            context["old_course"] = course_to_clone

            new_course = course_to_clone.clone(**new_course_data)

        elif request.path == "/courses/create":
            try:
                new_course = site.create_course(**new_course_data)
            except CourseTypeError as e:
                context["error"] = e.text

        if new_course:
            try:
                new_course.check(site)
            except AlreadyExistsError as e:
                context["error"] = e.text
            else:
                new_course.save(site)
                context["success"] = "Course created"

        return Response(render_template(template, context=context))
