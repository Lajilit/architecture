import os

from jinja2 import FileSystemLoader, TemplateNotFound, ChoiceLoader
from jinja2.environment import Environment, Template

from settings import INSTALLED_APPS, TEMPLATES_DIR, BASE_DIR


def render_template(template_name, folder=TEMPLATES_DIR, **kwargs):
    env = Environment()
    loaders = []
    for app in INSTALLED_APPS:
        path = os.path.join(BASE_DIR, app, folder)
        loaders.append(FileSystemLoader(path))
    env.loader = ChoiceLoader(loaders)
    try:
        template = env.get_template(template_name)
    except TemplateNotFound:
        path = os.path.join(
            os.path.dirname(__file__), "templates", "template_not_found.html"
        )
        with open(path, encoding="utf-8") as file:
            template = Template(file.read())
            return template.render(template_name=template_name)
    return template.render(**kwargs)


def get_view(request_path: str, url_patterns: list):
    for url in url_patterns:
        if url.url == request_path:
            return url.action
        if url.url != "/" and request_path.startswith(url.url):
            _, url_split = request_path.split(url.url)
            try:
                view = url.action(url_split)
            except TypeError:
                continue
            return view
