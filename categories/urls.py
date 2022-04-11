from framework.urls import URL
from categories.views import CategoryListView, CategoryCreateView


urlpatterns = [
    URL("/", CategoryListView()),
    URL("/create/", CategoryCreateView()),
]
