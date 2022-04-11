from framework.urls import URL, include
from categories.views import CategoryListView, CategoryCreateView
from core.views import MainView, ContactsView
from courses.views import CourseListView, CourseCreateView
from users.views import UserListView, UserCreateView

urlpatterns = [
    URL("/", MainView()),
    URL("/contacts", ContactsView()),
    # URL("/categories/", include(categories_patterns)),
    # URL("/courses/", include(courses_patterns)),
    # URL("/users/", include(users_patterns)),
    URL("/categories", CategoryListView()),
    URL("/categories/create", CategoryCreateView()),
    URL("/courses", CourseListView()),
    URL("/courses/create", CourseCreateView()),
    URL("/courses/clone", CourseCreateView()),
    # URL("/users", UserListView()),
    # URL("/users/create/", UserCreateView()),
]
