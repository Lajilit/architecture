import urllib


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
            request = {
                "method": environ.get("REQUEST_METHOD"),
                "data": self.get_request_data(environ),
                "params": self.get_request_params(environ),
            }

            for controller in self.front_controllers:
                controller(request, environ)

            code, text = view(request)
            start_response(code, self.headers)
            return [text.encode("utf-8")]

        else:
            start_response("404 Not found", self.headers)
            return [b"Page not found"]

    def get_request_data(self, environ):
        content_length = int(environ.get('CONTENT_LENGTH', '0'))
        data = environ["wsgi.input"].read(content_length) if content_length > 0 else b""
        data_str = data.decode(encoding="UTF-8")
        return self._parse_data(data_str)

    def get_request_params(self, environ):
        query_string = environ.get("QUERY_STRING")
        return self._parse_data(query_string)

    @staticmethod
    def _parse_data(data: str) -> dict:
        result = {}
        if data:
            params = data.split("&")
            for item in params:
                key, value = item.split("=")
                result[key] = urllib.parse.unquote_plus(value)
        return result
