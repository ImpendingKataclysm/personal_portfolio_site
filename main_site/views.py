from django.shortcuts import render
from django.views import generic
from . import models


class HomeView(generic.TemplateView):
    """
    Display the user information from the database on the home page.
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


class PortfolioView(generic.ListView):
    """
    Display the portfolio projects in the database on the Portfolio Page
    """
    queryset = models.PortfolioProject.objects.filter(is_active=True)
    template_name = 'portfolio.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['heading'] = 'Here are my recent projects'

        return context


class PortfolioProjectDetailView(generic.DetailView):
    """
    Display information from the selected Portfolio Project on the Portfolio
    Detail Page.
    """
    model = models.PortfolioProject
    template_name = 'portfolio_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioProjectDetailView, self).get_context_data()
        context['heading'] = str(self.get_object().name)

        return context
