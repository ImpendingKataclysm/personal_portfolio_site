from django.db import models
from django.contrib.auth.models import User

CHRFIELD_LEN = 200
TXTFIELD_LEN = 2000
MAX_NUM = 10

PRODUCT_TYPE = (
    ("bread", "Bread"),
    ("cakes", "Cakes"),
    ("pies", "Pies"),
    ("muffins", "Muffins"),
    ("assorted_pastries", "Assorted Pastries"),
    ("savoury_items", "Savoury Items"),
)


class Product(models.Model):
    """
    Database model for a bakery product.
    """
    name = models.CharField(max_length=CHRFIELD_LEN, blank=True, null=True)
    description = models.CharField(max_length=TXTFIELD_LEN, blank=True, null=True)
    price = models.DecimalField(max_digits=MAX_NUM, decimal_places=2)
    type = models.CharField(max_length=200, choices=PRODUCT_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    is_available = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='main_site')

    def __str__(self):
        return self.name


class Applicant(models.Model):
    """
    Database model for online job applications
    """
    first_name = models.CharField(max_length=CHRFIELD_LEN, blank=True, null=True)
    last_name = models.CharField(max_length=CHRFIELD_LEN, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=MAX_NUM, null=True, blank=True)
    date_available = models.DateField()
    resume = models.FileField(upload_to='resumes')
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


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
    name = models.CharField(verbose_name='Name', max_length=CHRFIELD_LEN)
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return f'{self.name}'


class Location(models.Model):
    """
    Defines a DB entry for the bakery's location. Contains the following fields:
    - street_address
    - city
    - postal
    - province
    - phone
    - email
    - image
    """
    street_address = models.CharField(max_length=CHRFIELD_LEN, blank=True, null=True)
    city = models.CharField(max_length=CHRFIELD_LEN, blank=True, null=True)
    postal = models.CharField(max_length=6)
    province = models.CharField(max_length=CHRFIELD_LEN)
    phone = models.CharField(max_length=MAX_NUM)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='project1', blank=True, null=True)

    def __str__(self):
        return f'{self.street_address} {self.city}, {self.province}'
