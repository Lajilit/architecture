from dataclasses import dataclass
from framework.views import View


@dataclass
class URL:
    url: str
    view: View
