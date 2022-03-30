import os.path
from core.models import CustomSite

BASE_DIR = os.path.dirname(__file__)

INSTALLED_APPS = [
    "core",
    "courses",
    "categories",
    "users",
]
TEMPLATES_DIR = "templates"
SITE = CustomSite()
