from django.db import models
from django.template.defaultfilters import slugify
from parler.models import TranslatableModel, TranslatedFields

# Maximum character lengths for text field values
NAME_MAX_LEN = 100
TEXT_MAX_LEN = 200

# Default integer field value
DEFAULT_INT = 80


class SiteOwner(TranslatableModel):
    """
    DB table that contains information about the site owner, including the
    following columns:
    - name
    - title
    - bio
    """
    translations = TranslatedFields(
        name=models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True),
        title=models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True),
        bio=models.TextField(max_length=TEXT_MAX_LEN, blank=True, null=True),
    )


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


class Certificate(TranslatableModel):
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

    translations = TranslatedFields(
        date=models.DateTimeField(blank=True, null=True),
        name=models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True),
        image=models.ImageField(blank=True, null=True, upload_to='media'),
        issued_by=models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True),
        description=models.CharField(max_length=TEXT_MAX_LEN, blank=True, null=True),
        is_active=models.BooleanField(default=True),
    )


class PortfolioProject(TranslatableModel):
    """
    DB table for portfolio projects displayed on the site. Contains the
    following columns:
    - date
    - name
    - description
    - slug
    - is_active
    - source_code_url: url for the source code on GitHub
    """

    class Meta:
        verbose_name_plural = 'Portfolio Projects'
        verbose_name = 'Portfolio Project'

    translations = TranslatedFields(
        name=models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True),
        description=models.CharField(max_length=TEXT_MAX_LEN, blank=True, null=True),
        slug=models.SlugField(null=True, blank=True),
        is_active=models.BooleanField(default=True),
        source_code_url=models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True),
        live_url=models.CharField(max_length=NAME_MAX_LEN, blank=True, null=True),
    )

    def save(self, *args, **kwargs):
        """
        If the project does not already exist, convert its name to a filename-
        compatible format and save it.
        @param args:
        @param kwargs:
        @return:
        """
        if not self.id:
            self.slug = slugify(self.translations.fields.get('name'))

        super(PortfolioProject, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        @return: The absolute url of the project including its parent directory
        filename
        """
        return f'/portfolio/{self.slug}'


class Image(TranslatableModel):
    """
    DB table for storing project images
    """
    image = models.ImageField(upload_to='portfolio', null=True, blank=True)

    project = models.ForeignKey(
        PortfolioProject,
        related_name='images',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    translations = TranslatedFields(
        caption=models.TextField(max_length=TEXT_MAX_LEN, null=True, blank=True),
    )


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
