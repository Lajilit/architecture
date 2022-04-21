from framework.errors import AlreadyExistsError, ModelTypeError, WrongCredentialsError
from framework.response import Response
from framework.service import render_template
from framework.views import View
from settings import SITE as site
from users.models import UserFactory

USER_TYPES = UserFactory.user_models


class UserListView(View):
    template = "users/user_list.html"

    @staticmethod
    def get_context(request):
        context = {
            "is_authorized": request.is_authorized,
            "user": request.user,
            "title": "Users",
            "header": "Users",
            "objects": site.users,
        }
        return context

    def get(self, request):
        context = self.get_context(request)
        return Response(render_template(self.template, context=context))


class UserCreateView(View):
    template = "users/user_register.html"

    @staticmethod
    def get_context(request):
        context = {
            "is_authorized": request.is_authorized,
            "user": request.user,
            "title": "Register new user",
            "header": "Register new user",
            "user_types": USER_TYPES,
        }
        return context

    def get(self, request):
        context = self.get_context(request)
        return Response(render_template(self.template, context=context))

    def post(self, request):
        context = self.get_context(request)
        try:
            password = request.data.get("password")
            password_2 = request.data.get("password_2")
            if password != password_2:
                raise WrongCredentialsError("Passwords are not the same")
        except WrongCredentialsError as e:
            context["error"] = e.text
        else:
            new_user_data = {
                "user_type": request.data.get("user_type"),
                "username": request.data.get("username"),
                "password": request.data.get("password"),
            }
            try:
                new_user = site.create_user(**new_user_data)
            except (ModelTypeError, AlreadyExistsError) as e:
                context["error"] = e.text
            else:
                new_user.save(site)
                context["success"] = f"New {new_user.user_type} registred"

        return Response(render_template(self.template, context=context))


class UserLoginView(View):
    template = "users/user_login.html"

    @staticmethod
    def get_context(request):
        context = {
            "is_authorized": request.is_authorized,
            "user": request.user,
            "title": "Log in",
            "header": "Log in",
        }
        return context

    def get(self, request):
        context = self.get_context(request)
        return Response(render_template(self.template, context=context))

    def post(self, request):
        context = self.get_context(request)

        user_data = {
            "username": request.data.get("username"),
            "password": request.data.get("password"),
        }
        try:
            site.login(**user_data)
        except WrongCredentialsError as e:
            context["error"] = e.text
        else:
            context["success"] = f"Successfully login"

        return Response(render_template(self.template, context=context))


class UserLogoutView(View):
    template = "users/user_logout.html"

    @staticmethod
    def get_context(request):
        context = {
            "is_authorized": request.is_authorized,
            "user": request.user,
            "title": "Logout",
            "header": "Logout",
        }
        return context

    def get(self, request):
        context = self.get_context(request)

        site.logout()
        context["success"] = f"Successfully logout"
        return Response(render_template(self.template, context=context))
