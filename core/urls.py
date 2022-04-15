from framework.urls import URL, include
from categories.urls import urlpatterns as categories_patterns
from core.views import MainView, ContactsView
from courses.urls import urlpatterns as courses_patterns
from users.urls import urlpatterns as users_patterns


urlpatterns = [
    URL("/", MainView()),
    URL("/contacts/", ContactsView()),
    URL("/categories", include(categories_patterns)),
    URL("/courses", include(courses_patterns)),
    URL("/users", include(users_patterns)),
]

# lesson_8