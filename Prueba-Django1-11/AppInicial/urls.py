from django.urls import path

from AppInicial.views import first_view

urlpatterns = [
    path('', first_view, name='first-view')
]
