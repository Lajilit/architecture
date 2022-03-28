from framework import Application

from study.urls import urlpatterns


def check_token(request):
    if request.authorization:
        request.is_authorized = True
    else:
        request.is_authorized = False
    return request


front_controllers = [check_token]


application = Application(urlpatterns, front_controllers)
