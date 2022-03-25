#Use framework

## Application structure example:
- your project
  - framework
  - your_app
    - templates
      - your_app
    - urls.py
    - views.py
  - main.py
  - settings.py


The name of the template folder must be specified 
in the TEMPLATES_DIR variable in the settings.py


The names of applications created in the project root must be specified 
as a list in the INSTALLED_APPS variable in the settings.py
## Settings file example:

`settings.py`
```import os.path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

INSTALLED_APPS = [
    "your_app"
]
TEMPLATES_DIR = "templates"
```

###To create your application use:
`main.py`
```
from framework import Application
from your_app.urls import urlpatterns

 #  your front controllers
    
front_controllers = [
  some_front_controller,
  ...
]
    
application = Application(urlpatterns, front_controllers)
```
####To create front_controllers use:
```
from framework.request import Request

def some_front_controller(request): 
    """
    some function that takes a Request() as parameter 
    and returns a Request()
    """
    # your code
    ...
    return request
```

###To create your urlpatterns use:
`urls.py`
```
from framework.urls import URL

urlpatterns = [
    URL("/some_url", SomeView()),
    ...
]
```



###To create some view use:
`views.py`
```
from framework.service import render_template
from framework.response import Response
from framework.views import View


class SomeView(View):
    def get(self, request):
        # some code
        ...
        context = {
        # some data to pass to the template
        }
        return Response(render_template("some_template.html", context=context))
```
The path to the template for render_template() must be specified starting from 
the folder specified in the TEMPLATES_DIR of the settings.py file
