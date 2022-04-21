from framework.urls import URL
from courses.views import CourseListView, CourseCreateView, CourseCloneView

urlpatterns = [
    URL("/", CourseListView()),
    URL("/create/", CourseCreateView()),
    URL("/clone/", CourseCloneView()),
]
