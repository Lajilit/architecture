from framework.response import Response


class View:
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options',
                         'trace']

    def run(self, request):
        return self.dispatch(request)

    def dispatch(self, request):
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(),
                              self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request)

    @staticmethod
    def http_method_not_allowed(request):
        return Response(f"Метод {request.method} не разрешен")


class NonFoundPageView(View):
    @staticmethod
    def get(request):
        return Response("404", f"{request.path}: Page not found")
