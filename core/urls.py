import core.views as views
from framework.urls import URL

urlpatterns = [
    URL("/", views.MainView()),
    URL("/about/", views.AboutView()),
    URL("/contacts/", views.ContactsView())
]
