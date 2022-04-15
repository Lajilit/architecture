from framework.urls import URL
from courses.views import (
    CourseListView,
    CourseCreateView,
    CourseCloneView,
    CourseRetrieveView,
)

urlpatterns = [
    URL("/", CourseListView()),
    URL("/create/", CourseCreateView()),
    URL("/clone/", CourseCloneView()),
    URL("/retrieve/", CourseRetrieveView()),
]
