import study.views as views
from framework.urls import URL

urlpatterns = [
    URL("/", views.MainView()),
    URL("/about/", views.AboutView()),
    URL("/contacts/", views.ContactsView()),
    URL("/create_course/", views.CreateCourseView()),
    URL("/clone_course/", views.CloneCourseView()),
]
