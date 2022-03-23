from framework import Application

from my_site.core.urls import urlpatterns


def check_token(request):
    if request.authorization:
        request.is_authorized = True
    else:
        request.is_authorized = False


front_controllers = [check_token]


application = Application(urlpatterns, front_controllers)
