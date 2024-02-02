from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from menu.models import Category, BarItem, BarCategory, Hookah


class MenuItemView(View):
    template_name = "menu/menu.html"

    def get(self, request, *args, **kwargs):
        categories = Category.objects.prefetch_related("menu_items", "bar_category_items").all()
        bar_categories = BarCategory.objects.all()
        context = {
            "categories": categories,
            "bar_categories": bar_categories
        }
        return render(request, self.template_name, context)


class BarItemView(View):
    template_name = "menu/menu.html"

    def get(self, request, *args, **kwargs):
        bar_items = BarCategory.objects.prefetch_related("bar_items", ).all()

        context = {
            "bar_items": bar_items,
        }

        return render(request, self.template_name, context)


class HookahListView(View):
    template_name = "menu/hookah.html"

    def get(self, request, *args, **kwargs):
        hookahs = Hookah.objects.all()
        context = {
            "hookahs": hookahs,
        }
        return render(request, self.template_name, context)


class BarItemDetailView(DetailView):
    model = BarItem
    template_name = "menu/bar_item_detail.html"
    context_object_name = "bar_item_detail"
    slug_url_kwarg = 'slug'
