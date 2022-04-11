from framework.urls import URL
from users.views import UserListView, UserCreateView

urlpatterns = [
    URL("/", UserListView()),
    URL("/create/", UserCreateView()),
]
