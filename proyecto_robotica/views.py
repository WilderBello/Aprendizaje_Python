from django.shortcuts import render

# Create your views here.

def home_robotica(request):
    return render(request, "home_robotica.html")
