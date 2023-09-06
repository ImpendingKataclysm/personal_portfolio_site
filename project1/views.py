from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'project1/home.html'


class AboutView(generic.TemplateView):
    template_name = 'project1/about.html'


class ContactView(generic.TemplateView):
    template_name = 'project1/contact.html'


class MenuView(generic.TemplateView):
    template_name = 'project1/menu.html'


class ReserveView(generic.TemplateView):
    template_name = 'project1/reserve.html'
