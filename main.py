from wsgiref.simple_server import make_server

from framework import front_controllers, Application

from my_site.core.urls import urlpatterns

application = Application(urlpatterns, front_controllers)

if __name__ == "__main__":
    host = "127.0.0.1"
    port = "80"

    with make_server(host, port, application) as http:
        print(f"Server started on {host}:{port}")
        http.serve_forever()
