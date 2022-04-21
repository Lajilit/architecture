import os.path
from core.models import CustomSite, BASE_DIR

INSTALLED_APPS = [
    "core",
    "courses",
    "categories",
    "users",
]
TEMPLATES_DIR = "templates"
SITE = CustomSite()
