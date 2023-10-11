from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from . import models, forms


class HomeView(generic.TemplateView):
    """
    Display the user information from the database on the home page.
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        skills = models.Skill.objects.all()
        certificates = models.Certificate.objects.all()
        projects = models.PortfolioProject.objects.all()

        context['skills'] = skills
        context['certificates'] = certificates
        context['projects'] = projects

        return context


class ContactView(generic.FormView):
    """
    Display the contact page with the contact form. When a message is received
    and successfully validated, it is stored in the Contact Messages table in
    the database and the user is redirected to the home page with a success
    message.
    """
    template_name = 'contact.html'
    form_class = forms.ContactForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['heading'] = 'Feel free to send me a message!'

        return context

    def form_valid(self, form):
        success_message = 'Thanks, I will be in touch soon!'
        form.save()
        messages.success(self.request, success_message)

        return super().form_valid(form)


class PortfolioView(generic.ListView):
    """
    Display the portfolio projects in the database on the Portfolio Page
    """
    queryset = models.PortfolioProject.objects.all()
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
