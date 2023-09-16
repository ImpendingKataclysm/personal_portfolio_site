from django.db import models

MAX_FIELD_LEN = 80
TXT_FIELD_LEN = 2000
PHONE_NUM_LEN = 10


class Employee(models.Model):
    """
    Database table for company employees whose profiles are displayed on the
    website.
    """
    first_name = models.CharField(max_length=MAX_FIELD_LEN)
    last_name = models.CharField(max_length=MAX_FIELD_LEN)
    role = models.CharField(max_length=MAX_FIELD_LEN)
    image = models.ImageField(upload_to='employees')

    def __str__(self):
        return f"{self.last_name}, {self.first_name}: {self.role}"


class ContactMessage(models.Model):
    """
    DB table for a message received from the Contact page. Contains the following
    columns:
    - timestamp
    - name: sender name
    - email: sender's email address
    - message: message content
    """
    class Meta:
        verbose_name_plural = 'Contact Messages'
        verbose_name = 'Contact Messages'

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='Name', max_length=MAX_FIELD_LEN)
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return f'{self.name}'


class Applicant(models.Model):
    """
    Database model for online job applications
    """
    first_name = models.CharField(max_length=MAX_FIELD_LEN, blank=True, null=True)
    last_name = models.CharField(max_length=MAX_FIELD_LEN, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=PHONE_NUM_LEN, null=True, blank=True)
    date_available = models.DateField()
    resume = models.FileField(upload_to='resumes')
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

