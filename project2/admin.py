from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')


@admin.register(models.Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name')


@admin.register(models.ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'timestamp')


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'province')
