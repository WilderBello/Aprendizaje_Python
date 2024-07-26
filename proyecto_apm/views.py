from django.shortcuts import render

# Create your views here.


def home_apm(request):
    return render(request, "home_apm.html")
