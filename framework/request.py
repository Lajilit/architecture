from urllib.parse import parse_qs


class Request:
    def __init__(self, environ: dict):
        self.method = environ.get("REQUEST_METHOD")
        self.path = environ.get("PATH_INFO")
        if not self.path.endswith("/"):
            self.path = f"{self.path}/"
        self.headers = self._get_headers(environ)
        self.data = self._get_request_data(environ)
        self.params = parse_qs(environ.get("QUERY_STRING"))
        self.authorization = environ.get("HTTP_AUTHORIZATION")
        self.is_authorized = False

    @staticmethod
    def _get_headers(env):
        headers = {}
        for key, value in env.items():
            if key.startswith("HTTP_"):
                headers[key[5:]] = value
        return headers

    @staticmethod
    def _get_request_data(env):
        content_length = int(env.get('CONTENT_LENGTH', '0'))
        data = env["wsgi.input"].read(content_length) if content_length > 0 else b""
        data_str = data.decode(encoding="UTF-8")
        return parse_qs(data_str)
