from dataclasses import dataclass
from typing import Union

from framework.service import get_view
from framework.views import View


class Include:
    def __init__(self, urlpatterns: list['URL']):
        self.urlpatterns = urlpatterns

    def __call__(self, path: str):
        view = get_view(path, self.urlpatterns)
        return view


include = Include


@dataclass
class URL:
    url: str
    view: Union[View, Include]
