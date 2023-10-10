from django.contrib import admin
from parler.admin import TranslatableAdmin
from . import models


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


admin.site.register(models.Skill, TranslatableAdmin)


@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'timestamp')
