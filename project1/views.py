from django.shortcuts import render
from django.views import generic
from . import models


class HomeView(generic.TemplateView):
    """
    Display Home Page
    """
    template_name = 'project1/home.html'


class AboutView(generic.TemplateView):
    """
    Display About Page
    """
    template_name = 'project1/about.html'


class ContactView(generic.TemplateView):
    template_name = 'project1/contact.html'


class MenuView(generic.ListView):
    """
    Display the Menu Page with the Menu Items from the database sorted by type
    """
    queryset = models.MenuItem.objects.order_by('-date_added')
    template_name = 'project1/menu.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MenuView, self).get_context_data()
        context['types'] = models.MENU_CATEGORIES

        return context


class MenuItemDetailView(generic.DetailView):
    model = models.MenuItem
    template_name = 'project1/menu_item_detail.html'


class ReserveView(generic.TemplateView):
    template_name = 'project1/reserve.html'
