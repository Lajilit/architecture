from framework import render_template
from framework.request import Request
from framework.response import Response
from framework.views import View


class MainView(View):
    def run(self, request: Request):
        context = {
            "title": "Main page",
            "text": "Main page",
            "description": "Some text",
        }
        return Response(render_template("index.html", context=context))


def main_page(request):
    context = {
        "has_token": request["is_authorized"],
        "title": "Main page",
        "text": "Main page",
        "description": "Some text",
    }
    code = "200 OK"
    return code, render_template("index.html", context=context)


def about_page(request):
    context = {"title": "About us", "text": "About us", "description": "Some text"}
    code = "200 OK"
    return code, render_template("index.html", context=context)


def contacts_page(request):
    if request.get('method') == 'POST':
        data = request.get("data")
        title = data.get("title")
        text = data.get("text")
        email = data.get("email")
        print(f"Получено сообщение от {email}:\n"
              f"Тема: {title}\n"
              f"Текст {text}")

    context = {
        "title": "Contacts",
        "text": "Our contacts",
        "email": "example123@gmail.com",
        "phone": "+7 800 123-45-67",
    }
    code = "200 OK"
    return code, render_template("contacts.html", context=context)
