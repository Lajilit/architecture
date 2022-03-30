from framework.urls import URL
from courses.views import CourseListView, CourseCreateView

urlpatterns = [
    URL("/", CourseListView()),
    URL("/create/", CourseCreateView()),
    URL("/clone/", CourseCreateView()),
]
