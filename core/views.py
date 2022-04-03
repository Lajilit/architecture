from framework.response import Response
from framework.service import render_template
from framework.views import View
from settings import SITE as site


class MainView(View):
    @staticmethod
    def get(request):
        context = {
            "is_authorized": request.is_authorized,
            "title": "Courses list",
            "header": "Courses list",
            "courses_list": site.courses,
        }
        return Response(render_template("/core/index.html", context=context))


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
            "title": "Contacts",
            "text": "Our contacts",
            "email": "example123@gmail.com",
            "phone": "+7 800 123-45-67",
            "success": "We received your message",
        }

        return Response(render_template("core/contacts.html", context=context))

    @staticmethod
    def get(request):
        context = {
            "is_authorized": request.is_authorized,
            "title": "Contacts",
            "text": "Our contacts",
            "email": "example123@gmail.com",
            "phone": "+7 800 123-45-67",
        }
        return Response(render_template("core/contacts.html", context=context))
