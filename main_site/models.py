from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Maximum character lengths for text field values
NAME_MAX_LEN = 100
TEXT_MAX_LEN = 200

# Default integer field value
DEFAULT_INT = 80


class Skill(models.Model):
    """
    Database table that contains the site user's skills. Contains the following
    columns:
    - name
    - score: Percentage that represents the user's level of proficiency with
    the skill
    - image: URL for an image/icon to be displayed with the skill
    - is_key: Indicates whether this is a key (personal/life) skill
    or a professional/programming skill
    """

    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    name = models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True)
    score = models.IntegerField(default=DEFAULT_INT, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='skills')
    is_key = models.BooleanField(default=False)

    def __str__(self):
        """
        @return: The name of the skill
        """
        return self.name


class UserProfile(models.Model):
    """
    Database table that contains information about the site user (this should be
    the only row in the table). Contains the following columns:
    - user: Authorized site user
    - title: User's current title/role
    - bio
    - skills: List of all Skills registered in the database
    - cv: User's resume available for download
    """
    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatar')
    title = models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to='cv')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Media(models.Model):
    """
    DB table that contains media files the user has uploaded to the site. Contains
    the following columns:
    - image: filename for an image file
    - url: url for a media file that is not an image
    - name
    - is_image: indicates whether the file is an image
    """
    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ['name']

    image = models.ImageField(blank=True, null=True, upload_to='media')
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """
        Saves media file after checking whether it is an image. Sets is_image
        to False if the file has a non-image url
        @param args:
        @param kwargs:
        @return:
        """
        if self.url:
            self.is_image = False

        super(Media, self).save(*args, **kwargs)


class Certificate(models.Model):
    """
    DB table that contains certificates the user has earned. Contains the
    following columns:
    - date: Date awarded
    - name
    - issued_by: Issuing authority/institution
    - description
    - is_active
    """
    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='media')
    issued_by = models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True)
    description = models.CharField(max_length=TEXT_MAX_LEN, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
