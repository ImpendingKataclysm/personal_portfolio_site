from django.contrib import admin
from parler.admin import TranslatableAdmin
from . import models

admin.site.register(models.Skill, TranslatableAdmin)
admin.site.register(models.PortfolioProject, TranslatableAdmin)
admin.site.register(models.Certificate, TranslatableAdmin)


@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'timestamp')
