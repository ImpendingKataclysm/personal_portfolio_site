from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

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

    name = models.CharField(_('name'), max_length=NAME_MAX_LEN, blank=True, null=True)
    image = models.FileField(_('image'), blank=True, null=True, upload_to='skills')
    is_key = models.BooleanField(_('is_key'), default=False)

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


class PortfolioProject(models.Model):
    """
    DB table for portfolio projects displayed on the site. Contains the
    following columns:
    - date
    - name
    - description
    - image
    - slug
    - is_active
    - source_code_url: url for the source code on GitHub
    """
    class Meta:
        verbose_name_plural = 'Portfolio Projects'
        verbose_name = 'Portfolio Project'
        ordering = ['name']

    date = models.DateTimeField(blank=True)
    name = models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True)
    description = models.CharField(max_length=TEXT_MAX_LEN, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='portfolio')
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    source_code_url = models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True)
    live_url = models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        If the project does not already exist, convert its name to a filename-
        compatible format and save it.
        @param args:
        @param kwargs:
        @return:
        """
        if not self.id:
            self.slug = slugify(self.name)

        super(PortfolioProject, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        @return: The absolute url of the project including its parent directory
        filename
        """
        return f'/portfolio/{self.slug}'

    def __str__(self):
        return self.name


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
    name = models.CharField(verbose_name='Name', max_length=NAME_MAX_LEN)
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return f'{self.name}'
