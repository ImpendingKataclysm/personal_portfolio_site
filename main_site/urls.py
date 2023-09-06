from django.urls import path
from . import views

import project1.views as project1

app_name = 'main_site'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('project/<slug:slug>', views.PortfolioProjectDetailView.as_view(), name='portfolio_detail'),
    path('portfolio/project1/', project1.HomeView.as_view(), name='project1')
]
