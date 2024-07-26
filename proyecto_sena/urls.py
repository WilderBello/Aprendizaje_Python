from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_adsi, name='home_adsi')
]
