from django.db import models
from django.contrib.auth.models import User

NAME_MAX_LEN = 100
TEXT_MAX_LEN = 2000
MAX_NUM = 10

MENU_CATEGORIES = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Desserts'),
    ('drinks', 'Drinks'),
)


class MenuItem(models.Model):
    """
    Defines a database entry for a menu item. Contains the following fields:
    - name
    - description
    - price
    - type (must be one of the MENU_CATEGORIES)
    - author
    - is_available
    - date_added
    - image
    """
    name = models.CharField(
        max_length=NAME_MAX_LEN,
        unique=True,
        blank=True,
        null=True
    )

    description = models.CharField(max_length=TEXT_MAX_LEN, blank=True, null=True)

    price = models.DecimalField(
        max_digits=MAX_NUM,
        decimal_places=2,
        blank=True,
        null=True
    )

    type = models.CharField(
        max_length=NAME_MAX_LEN,
        choices=MENU_CATEGORIES,
        blank=True,
        null=True
    )

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    is_available = models.BooleanField(default=True, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to='project1', blank=True, null=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    """
    Defines a DB entry for a restaurant location. Contains the following fields:
    - street_address
    - city
    - postal
    - province
    - phone
    """
    street_address = models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True)
    city = models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True)
    postal = models.CharField(max_length=6)
    province = models.CharField(max_length=NAME_MAX_LEN)
    phone = models.CharField(max_length=MAX_NUM)
    image = models.ImageField(upload_to='project1', blank=True, null=True)

    def __str__(self):
        return f'{self.street_address} {self.city}, {self.province}'


class Reservation(models.Model):
    """
    Defines a DB entry for a Reservation. Contains the following fields:
    - party_name
    - party_size
    - phone
    - email
    - location
    - date
    - time
    - booked_on: Date the reservation was made
    """
    party_name = models.CharField(max_length=NAME_MAX_LEN)
    party_size = models.IntegerField()
    phone = models.CharField(max_length=MAX_NUM)
    email = models.EmailField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.party_name}, {self.date}'
