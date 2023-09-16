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
        max_length=models.MAX_FIELD_LEN,
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
        max_length=models.TXT_FIELD_LEN,
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


class ApplicantForm(forms.ModelForm):
    """
    Defines the job application form. Contains the following fields:
    - first_name (CharField)
    - last_name (CharField)
    - email (EmailField
    - phone (CharField)
    - date_available (DateField)
    - resume (FileField)
    Applicant data is stored in the database and uploaded resumes are stored in
    mediafiles/resumes.
    """
    first_name = forms.CharField(
        max_length=models.TXT_FIELD_LEN,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your first name',
        }),
    )

    last_name = forms.CharField(
        max_length=models.TXT_FIELD_LEN,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your last name',
        }),
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email address',
        }),
    )

    phone = forms.CharField(
        max_length=models.PHONE_NUM_LEN,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your phone number',
        }),
    )

    date_available = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
        }),
    )

    resume = forms.FileField()

    class Meta:
        model = models.Applicant
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'date_available',
            'resume',
        )
