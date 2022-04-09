from framework.errors import AlreadyExistsError
from framework.response import Response
from framework.service import render_template
from framework.views import View
from settings import SITE as site


class CategoryListView(View):
    template = "categories/categories_list.html"

    @staticmethod
    def get_context(request):
        context = {
            "is_authorized": request.is_authorized,
            "title": "Course categories",
            "header": "Course categories",
            "objects": site.base_category.tree(),
        }
        return context

    def get(self, request):
        context = self.get_context(request)
        return Response(render_template(self.template, context=context))


class CategoryCreateView(View):
    template = "categories/category_create.html"

    @staticmethod
    def get_context(request):
        context = {
            "is_authorized": request.is_authorized,
            "title": "Create category",
            "header": "Create category",
        }
        return context

    def get(self, request):
        context = self.get_context(request)
        context["categories"] = site.base_category.tree()
        return Response(render_template(self.template, context=context))

    def post(self, request):
        context = self.get_context(request)
        context["categories"] = site.base_category.tree()
        parent_category_id = int(request.data.get("parent_category"))
        parent_category = site.get_category(parent_category_id)
        try:
            new_category = site.create_category(
                category_name=request.data.get("category_name"),
                parent=parent_category,
            )
        except AlreadyExistsError as e:
            context["error"] = e.text
        else:
            new_category.save()
            context["success"] = "Category created"

        return Response(render_template(self.template, context=context))
