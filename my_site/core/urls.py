import my_site.core.views as views
from framework.urls import URL

# urlpatterns = {
#     "/": views.main_page,
#     "/about/": views.about_page,
#     "/contacts/": views.contacts_page,
# }


urlpatterns = [
    URL("/", views.MainView())
]
