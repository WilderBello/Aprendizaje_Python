from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_robotica, name='home_robotica')
]
