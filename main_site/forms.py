from django import forms
from . import models


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=models.NAME_MAX_LEN,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your name',
        })
    )

    email = forms.EmailField(
        max_length=320,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email',
        })
    )

    message = forms.CharField(
        max_length=models.TEXT_MAX_LEN,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Message',
            'rows': 6,
        })
    )

    class Meta:
        model = models.ContactMessage
        fields = ('name', 'email', 'message')
