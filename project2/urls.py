from django.urls import path
from . import views

app_name = 'project2'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('products/', views.ProductPage.as_view(), name='products'),
    path('jobs/', views.JobsPage.as_view(), name='jobs'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
]
