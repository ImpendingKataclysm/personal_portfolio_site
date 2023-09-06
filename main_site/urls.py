from django.urls import path
from . import views

app_name = 'main_site'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('project/<slug:slug>', views.PortfolioProjectDetailView.as_view(), name='portfolio_detail'),
]
