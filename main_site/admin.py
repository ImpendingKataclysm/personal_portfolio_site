from django.contrib import admin
from . import models


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
