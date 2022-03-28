from framework.response import Response
from framework.service import render_template
from framework.views import View
from study.models import CustomSite, CourseFactory

site = CustomSite()


class MainView(View):
    @staticmethod
    def get(request):
        context = {
            "is_authorized": request.is_authorized,
            "title": "Courses list",
            "header": "Courses list",
            "courses_list": site.courses,
        }
        return Response(render_template("study/index.html", context=context))


class CreateCourseView(View):
    @staticmethod
    def post(request):
        data = request.data
        course_name = data.get("course_name")[0]
        course_type = data.get("course_type")[0]
        old_course = site.get_course(course_name, course_type)
        if old_course:
            return Response(
                render_template(
                    "study/create_course.html",
                    context={"error": "course already exists"},
                )
            )
        course = site.create_course(course_type, course_name)
        if course:
            site.courses.append(course)
        else:
            return Response(
                render_template(
                    "study/create_course.html", context={"error": "wrong course_type"}
                )
            )
        return Response(
            render_template(
                "study/course_created.html",
                context={"course_name": course_name, "course_type": course_type},
            )
        )

    @staticmethod
    def get(request):
        context = {
            "is_authorized": request.is_authorized,
            "title": "Create course",
            "header": "Create course",
        }
        return Response(render_template("study/create_course.html", context=context))


class CloneCourseView(View):
    @staticmethod
    def get(request):
        params = request.params
        clone_course_name = params.get("course_name")[0]
        clone_course_type = params.get("course_type")[0]
        clone_course = site.get_course(clone_course_name, clone_course_type)
        if clone_course:
            context = {
                "is_authorized": request.is_authorized,
                "title": "Clone course",
                "header": "Clone course",
                "old_course": clone_course,
            }
            return Response(render_template("study/clone_course.html", context=context))

    @staticmethod
    def course_exists(name, type):
        return site.get_course(name, type)

    def post(self, request):
        data = request.data

        clone_course_name = data.get("old_course_name")[0]
        clone_course_type = data.get("old_course_type")[0]
        clone_course = site.get_course(clone_course_name, clone_course_type)

        new_course_name = data.get("course_name", [clone_course_name])[0]
        new_course_type = data.get("course_type", [clone_course_type])[0]

        new_course = clone_course.clone(new_course_name, new_course_type)

        if self.course_exists(new_course_name, new_course_type):
            template = "study/clone_course.html"
            context = {
                "is_authorized": request.is_authorized,
                "title": "Clone course",
                "header": "Clone course",
                "old_course": clone_course,
                "error": "course already exists",
            }
        elif new_course.type not in CourseFactory.course_types.keys():
            template = "study/clone_course.html"
            context = {
                "is_authorized": request.is_authorized,
                "title": "Clone course",
                "header": "Clone course",
                "old_course": clone_course,
                "error": "wrong course_type",
            }
        else:
            site.courses.append(new_course)
            template = "study/course_created.html"
            context = {
                "is_authorized": request.is_authorized,
                "title": "Course created",
                "header": "Course created",
                "course_name": new_course_name,
                "course_type": new_course_type,
            }

        return Response(render_template(template, context=context))


class AboutView(View):
    @staticmethod
    def get(request):
        context = {
            "is_authorized": request.is_authorized,
            "title": "About us",
            "text": "About us",
            "description": "Some text",
        }
        return Response(render_template("study/about.html", context=context))


class ContactsView(View):
    @staticmethod
    def post(request):
        data = request.data
        title = data.get("title")
        text = data.get("text")
        email = data.get("email")
        print(f"Получено сообщение от {email}:\n" f"Тема: {title}\n" f"Текст {text}")

        context = {
            "is_authorized": request.is_authorized,
            "title": "Thank you",
            "text": "We received your message",
        }

        return Response(render_template("study/thanks.html", context=context))

    @staticmethod
    def get(request):
        context = {
            "is_authorized": request.is_authorized,
            "title": "Contacts",
            "text": "Our contacts",
            "email": "example123@gmail.com",
            "phone": "+7 800 123-45-67",
        }
        return Response(render_template("study/contacts.html", context=context))
