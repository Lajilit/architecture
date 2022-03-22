from framework.request import Request
from framework.response import Response


class View:
    pass


class NonFoundPageView(View):
    def run(self, request: Request):
        return Response("404", "Page not found")
