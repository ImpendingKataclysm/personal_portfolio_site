from django.urls import path
from . import views

app_name = 'project1'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('item/<int:pk>', views.MenuItemDetailView.as_view(), name='menu_item'),
    path('reserve/', views.ReserveView.as_view(), name='reserve'),
]
