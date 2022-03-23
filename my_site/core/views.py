from framework import render_template
from framework.response import Response
from framework.views import View


class MainView(View):
    @staticmethod
    def get(request):
        context = {
            "is_authorized": request.is_authorized,
            "title": "Main page",
            "text": "Main page",
            "description": "Some text",
        }
        return Response(render_template("core/index.html", context=context))


class AboutView(View):
    @staticmethod
    def get(request):
        context = {
            "is_authorized": request.is_authorized,
            "title": "About us",
            "text": "About us",
            "description": "Some text"}
        return Response(render_template("core/about.html", context=context))


class ContactsView(View):

    @staticmethod
    def post(request):
        data = request.data
        title = data.get("title")
        text = data.get("text")
        email = data.get("email")
        print(f"Получено сообщение от {email}:\n"
              f"Тема: {title}\n"
              f"Текст {text}")

        context = {
            "is_authorized": request.is_authorized,
            "title": "Thank you",
            "text": "We received your message"
        }

        return Response(render_template("core/thanks.html", context=context))

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


