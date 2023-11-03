from django.urls import path

import project2.views
import project3.views
from . import views

import project1.views as project1

app_name = 'main_site'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('portfolio/project1/', project1.HomeView.as_view(), name='project1'),
    path('portfolio/project2/', project2.views.HomePage.as_view(), name='project2'),
    path('portfolio/project3/', project3.views.HomePage.as_view(), name='project3'),
]
