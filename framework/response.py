class Response:
    def __init__(self, body, status_code="200 OK"):
        self.headers = [("Content-type", "text/html")]
        self.status_code = str(status_code)
        self.body = body.encode('utf-8')
