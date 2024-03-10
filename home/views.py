from django.views import View
from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from .models import Chef, Gallery, Events
from menu.models import Category, MenuItem, BarCategory, Hookah


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['menu_items'] = MenuItem.objects.select_related("category").all()
        context['bar_categories'] = BarCategory.objects.all()
        context['hookahs'] = Hookah.objects.all()
        context['events'] = Events.objects.all()
        context['our_chefs'] = Chef.objects.all()
        context['gallery_images'] = Gallery.objects.all()
        return context


class AboutUsView(TemplateView):
    template_name = 'home/about.html'


class ContactUsView(TemplateView):
    template_name = 'home/contact_us.html'


class ChefUsView(View):
    template_name = "home/chefs.html"

    def get(self, request, *args, **kwargs):
        our_chefs = Chef.objects.all()
        context = {
            'our_chefs': our_chefs,
        }
        return render(request, self.template_name, context)


class GalleryView(ListView):
    model = Gallery
    template_name = 'home/gallery.html'
    context_object_name = 'gallery_images'


class EventsView(TemplateView):
    template_name = "home/events.html"

    def get(self, request, *args, **kwargs):
        events = Events.objects.all()

        context = {
            'events': events,
        }

        return render(request, self.template_name, context)
