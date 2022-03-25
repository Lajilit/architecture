from framework import render_template


def main_page(request):
    context = {
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
    context = {
        "title": "Contacts",
        "text": "Our contacts",
        "email": "example123@gmail.com",
        "phone": "+7 800 123-45-67",
    }
    code = "200 OK"
    return code, render_template("contacts.html", context=context)
