from framework.request import Request
from framework.views import NonFoundPageView


class Application:
    def __init__(self, url_patterns, front_controllers):
        self.url_patterns = url_patterns
        self.front_controllers = front_controllers

    def __call__(self, environ, start_response):
        """
        :param environ: словарь данных от сервера
        :param start_response: функция для ответа серверу
        """

        request = Request(environ)
        for controller in self.front_controllers:
            controller(request)
        view = self.get_view(request)
        response = view.run(request)
        start_response(response.status_code, response.headers)
        return [response.body]

    def get_view(self, request):
        for url in self.url_patterns:
            if url.url == request.path:
                return url.view
        return NonFoundPageView()
