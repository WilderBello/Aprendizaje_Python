from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
]
