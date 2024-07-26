from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_apm, name='home_apm')
]
