from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from . import models, forms


class HomeView(generic.TemplateView):
    """
    Display the Home Page
    """
    template_name = 'project1/home.html'


class AboutView(generic.TemplateView):
    """
    Display About Page
    """
    template_name = 'project1/about.html'


class LocationView(generic.ListView):
    """
    Display contact information for each restaurant location registered in the
    database.
    """
    queryset = models.Location.objects.order_by('city')
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
    """
    Display the details of the specified menu item
    """
    model = models.MenuItem
    template_name = 'project1/menu_item_detail.html'


class ReserveView(generic.FormView):
    template_name = 'project1/reserve.html'
    form_class = forms.ReservationForm
    success_url = '/project1/'

    def form_valid(self, form):
        success_message = 'Thanks, we look forward to seeing you!'
        form.save()
        messages.success(self.request, success_message)

        return super().form_valid(form)
