import json

from django.views import generic
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from . import models, forms


class HomeView(generic.TemplateView):
    """
    Display the user information from the database on the home page.
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        me = models.SiteOwner.objects.first()
        certificates = models.Certificate.objects.all()
        projects = models.PortfolioProject.objects.all()

        context['me'] = me
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

    def form_valid(self, form):
        language = self.request.LANGUAGE_CODE
        success_message = 'Thanks, I will be in touch soon!'

        if language == 'fr':
            success_message = "Merci, je vous contacterai bientôt!"
            self.success_url = '/fr/'

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
        context = super(PortfolioView, self).get_context_data(**kwargs)

        json_data = json.dumps(
            list(models.PortfolioProject.objects.values()),
            cls=DjangoJSONEncoder
        )

        context['object_list_json'] = json_data

        return context
