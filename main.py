from core.urls import urlpatterns
from framework import Application
from settings import SITE as site
from settings import BASE_DIR


def check_token(request):
    with open(f"{BASE_DIR}/token.txt", "r") as f:
        token = f.read()
    if token:
        request.is_authorized = True
        request.user = site.get_user(token=token)
    else:
        request.is_authorized = False
    return request


front_controllers = [check_token]

application = Application(urlpatterns, front_controllers)
