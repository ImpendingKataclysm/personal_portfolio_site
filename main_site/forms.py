from django import forms
from . import models


class ContactForm(forms.ModelForm):
    """
    Defines the contact page form through which visitors may send the site
    admin messages. Contains the following fields:
    - name: sender name
    - email: sender email address
    - message: message content
    Data send via the contact form is stored in the Contact Messages table in
    the database.
    """
    name = forms.CharField(
        max_length=models.NAME_MAX_LEN,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )

    email = forms.EmailField(
        max_length=320,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )

    message = forms.CharField(
        max_length=models.TEXT_MAX_LEN,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 6,
        })
    )

    class Meta:
        model = models.ContactMessage
        fields = ('name', 'email', 'message')
