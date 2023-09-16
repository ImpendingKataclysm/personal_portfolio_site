from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from . import models, forms


class HomePage(generic.TemplateView):
    """
    Display the home page
    """
    template_name = 'project3/index.html'


class AboutPage(generic.TemplateView):
    """
    Display the about page
    """
    template_name = 'project3/about.html'


class TeamPage(generic.ListView):
    """
    Display the employee data stored in the database on the Team Page
    """
    queryset = models.Employee.objects.order_by('last_name')
    template_name = 'project3/team.html'


class ContactPage(generic.FormView):
    """
    Display the contact page with the contact form. When a message is received
    and successfully validated, it is stored in the Contact Messages table in
    the database and the user is redirected to the home page with a success
    message.
    """
    form_class = forms.ContactForm
    template_name = 'project3/contact.html'
    success_url = '/project3/'

    def form_valid(self, form):
        success_message = 'Thank you, we will be in touch soon.'
        form.save()
        messages.success(self.request, success_message)
        
        return super(ContactPage, self).form_valid(form)


class CareersPage(generic.FormView):
    """
    Display job application form on the Careers page. When the form is submitted,
    save the applicant to the database
    """
    form_class = forms.ApplicantForm
    template_name = 'project3/careers.html'
    success_url = '/project3/'
    
    def form_valid(self, form):
        success_message = 'Thank you for your application.'
        applicant = form.save(commit=False)
        
        applicant.save()
        messages.success(self.request, message=success_message)
        
        return super(CareersPage, self).form_valid(form)
