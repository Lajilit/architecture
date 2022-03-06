from os.path import join

from jinja2 import Template

from my_site.core.settings import TEMPLATES_DIR


def render_template(template_name, **kwargs):

    path = join(TEMPLATES_DIR, template_name)

    with open(path, encoding="utf-8") as file:
        template = Template(file.read())

        return template.render(**kwargs)
