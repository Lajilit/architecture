class NotFoundPage:
    def __call__(self, request):
        return "404 Not found", "Page not found"


class Application:
    def __init__(self, url_patterns, front_controllers):
        self.url_patterns = url_patterns
        self.front_controllers = front_controllers
        self.headers = [("Content-Text", "file/html")]

    def __call__(self, environ, start_response):
        """
        :param environ: словарь данных от сервера
        :param start_response: функция для ответа серверу
        """
        path = environ.get("PATH_INFO")
        if not path.endswith("/"):
            path = f"{path}/"

        if path in self.url_patterns:
            view = self.url_patterns.get(path)
        else:
            view = NotFoundPage()
        request = {}
        for controller in self.front_controllers:
            controller(request, environ)
        if request.get("is_authorized"):
            code, text = view(request)
        else:
            code = "403 Forbidden"
            text = "no token"
        start_response(code, self.headers)
        return [text.encode("utf-8")]
