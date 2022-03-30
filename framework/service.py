import os

from jinja2 import FileSystemLoader, TemplateNotFound
from jinja2.environment import Environment, Template

from settings import INSTALLED_APPS, TEMPLATES_DIR, BASE_DIR


def render_template(template_name, folder=TEMPLATES_DIR, **kwargs):
    for app in INSTALLED_APPS:
        path = os.path.join(BASE_DIR, app, folder)
        env = Environment()
        env.loader = FileSystemLoader(path)
        try:
            template = env.get_template(template_name)
        except TemplateNotFound:
            continue
        return template.render(**kwargs)

    path = os.path.join(
        os.path.dirname(__file__), "templates", "template_not_found.html"
    )
    with open(path, encoding="utf-8") as file:
        template = Template(file.read())
        return template.render(template_name=template_name)


def get_view(request_path: str, url_patterns: list):
    for url in url_patterns:
        if url.url == request_path:
            return url.view
        elif url.url != "/" and request_path.startswith(url.url):
            url_split = request_path.lstrip(url.url)
            view = url.view(url_split, url_patterns)
            return view
