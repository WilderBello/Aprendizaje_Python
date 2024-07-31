from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_apm, name='home_apm'),
]
