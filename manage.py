from pprint import pprint


def application(environ, start_response):
    """
    :param environ: словарь данных от сервера
    :param start_response: функция для ответа серверу
    """
    pprint(environ)
    path = environ.get("PATH_INFO")
    if path == "/index":
        start_response('200 OK', [('Content-Type', 'text/html')])
        # возвращаем тело ответа в виде списка из bite
        return [b'Index page']
    elif path == "/about":
        start_response('200 OK', [('Content-Type', 'text/html')])
        # возвращаем тело ответа в виде списка из bite
        return [b'About page']
    else:
        # сначала в функцию start_response передаем код ответа и заголовки
        start_response('404 Not found', [('Content-Type', 'text/html')])
        # возвращаем тело ответа в виде списка из bite
        return [b'Page not found']
