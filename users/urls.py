from framework.urls import URL
from users.views import UserListView, UserCreateView, UserLoginView, UserLogoutView

urlpatterns = [
    URL("/", UserListView()),
    URL("/register/", UserCreateView()),
    URL("/login/", UserLoginView()),
    URL("/logout/", UserLogoutView()),
]
