from django.urls import path
from . import views

app_name = 'project3'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('team/', views.TeamPage.as_view(), name='team'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('careers/', views.CareersPage.as_view(), name='careers'),
]
