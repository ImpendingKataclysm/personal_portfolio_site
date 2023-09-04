from django.shortcuts import render
from django.views import generic
from . import models


class HomeView(generic.TemplateView):
    """
    Display the home page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        skills = models.Skill.objects.all()
        certificates = models.Certificate.objects.filter(is_active=True)
        projects = models.PortfolioProject.objects.filter(is_active=True)

        context['skills'] = skills
        context['certificates'] = certificates
        context['projects'] = projects

        return context


class ContactView(generic.TemplateView):
    template_name = 'contact.html'


class PortfolioView(generic.TemplateView):
    template_name = 'portfolio.html'


class PortfolioDetailView(generic.DetailView):
    model = models.PortfolioProject
    template_name = 'portfolio_detail.html'
