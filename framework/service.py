import os
from os.path import join
from jinja2 import FileSystemLoader, TemplateNotFound
from jinja2.environment import Environment, Template

from settings import INSTALLED_APPS, TEMPLATES_DIR, BASE_DIR


def render_template(template_name, folder=TEMPLATES_DIR, **kwargs):
    print(BASE_DIR)
    for app in INSTALLED_APPS:
        path = join(BASE_DIR, app, folder)
        env = Environment()
        env.loader = FileSystemLoader(path)
        try:
            template = env.get_template(template_name)
        except TemplateNotFound:
            continue
        return template.render(**kwargs)

    path = join(os.path.dirname(__file__), "templates", "template_not_found.html")
    with open(path, encoding="utf-8") as file:
        template = Template(file.read())
        return template.render(template_name=template_name)

