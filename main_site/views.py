from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    """
    Display the home page
    """
    template_name = 'index.html'


class ContactView(generic.TemplateView):
    template_name = 'contact.html'
