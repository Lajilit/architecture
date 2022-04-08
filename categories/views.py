from core.errors import AlreadyExistsError
from framework.response import Response
from framework.service import render_template
from framework.views import View
from settings import SITE as site


class CategoryListView(View):
    @staticmethod
    def get(request):
        context = {
            "is_authorized": request.is_authorized,
            "title": "Course categories",
            "header": "Course categories",
            "categories": site.base_category.tree(),
        }
        return Response(
            render_template("categories/categories_list.html", context=context)
        )


class CategoryCreateView(View):
    def get(self, request):
        template = "categories/category_create.html"
        context = {
            "is_authorized": request.is_authorized,
            "title": "Create category",
            "header": "Create category",
            "categories": site.base_category.tree(),
        }
        return Response(render_template(template, context=context))

    def post(self, request):
        template = "categories/category_create.html"
        context = {
            "is_authorized": request.is_authorized,
            "title": "Create category",
            "header": "Create category",
        }
        parent_category_id = int(request.data.get("parent_category")[0])
        parent_category = site.get_category(parent_category_id)
        if not parent_category:
            parent_category = site.base_category

        try:
            new_category = site.create_category(
                category_name=request.data.get("category_name")[0],
                parent=parent_category,
            )
        except AlreadyExistsError as e:
            context["error"] = e.text
        else:
            new_category.save()
            context["success"] = "Category created"

        return Response(render_template(template, context=context))
