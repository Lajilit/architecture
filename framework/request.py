from urllib.parse import parse_qsl

from .errors import AlreadyExistsError


class Request:
    def __init__(self, environ: dict):
        self.method = environ.get("REQUEST_METHOD")
        self.path = environ.get("PATH_INFO")
        if not self.path.endswith("/"):
            self.path = self.path + "/"
        self.headers = self._get_headers(environ)
        self.data = self._get_request_data(environ)
        self.params = self.parse_qs(environ.get("QUERY_STRING"))
        self.user = None
        self.is_authorized = False

    @staticmethod
    def _get_headers(env):
        headers = {}
        for key, value in env.items():
            if key.startswith("HTTP_"):
                headers[key[5:]] = value
        return headers

    def _get_request_data(self, env):
        content_length = int(env.get("CONTENT_LENGTH", "0"))
        data = env["wsgi.input"].read(content_length) if content_length > 0 else b""
        data_str = data.decode(encoding="UTF-8")
        parsed_data = self.parse_qs(data_str)
        return parsed_data

    @staticmethod
    def parse_qs(
        qs,
        keep_blank_values=False,
        strict_parsing=False,
        encoding="utf-8",
        errors="replace",
        max_num_fields=None,
        separator="&",
    ):
        parsed_result = {}
        pairs = parse_qsl(
            qs,
            keep_blank_values,
            strict_parsing,
            encoding=encoding,
            errors=errors,
            max_num_fields=max_num_fields,
            separator=separator,
        )
        for name, value in pairs:
            if name in parsed_result:
                raise AlreadyExistsError(f"Duplicated parameter {name} in request")
            else:
                parsed_result[name] = value
        return parsed_result
