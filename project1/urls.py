from django.urls import path
from . import views

app_name = 'rest_demo'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]
