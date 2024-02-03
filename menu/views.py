from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from menu.models import Category, BarItem, BarCategory, Hookah


class MenuListView(ListView):
    template_name = "menu/menu.html"
    context_object_name = 'categories'  # This sets the variable name in the template

    def get_queryset(self):
        return Category.objects.prefetch_related("menu_items", "bar_category_items").all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bar_categories'] = BarCategory.objects.all()
        return context


class BarListView(ListView):
    template_name = "menu/menu.html"
    context_object_name = 'bar_categories'  #

    def get_queryset(self):
        return BarCategory.objects.prefetch_related("bar_items").all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HookahListView(View):
    template_name = "menu/hookah.html"

    def get(self, request, *args, **kwargs):
        hookahs = Hookah.objects.all()
        context = {
            "hookahs": hookahs,
        }
        return render(request, self.template_name, context)


class BarCategoryDetailView(DetailView):
    model = BarCategory
    template_name = "menu/bar_item_detail.html"
    context_object_name = "bar_item_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bar_items'] = self.object.bar_items.all()
        return context


class BarItemDetailView(DetailView):
    model = BarItem
    template_name = "menu/bar_item_detail.html"
    context_object_name = "bar_item_detail"
