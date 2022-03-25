import my_site.core.views as views

urlpatterns = {
    "/": views.main_page,
    "/about/": views.about_page,
    "/contacts/": views.contacts_page,
}
