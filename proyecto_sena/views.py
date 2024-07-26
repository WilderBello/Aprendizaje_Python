from django.shortcuts import render

# Create your views here.


def home_adsi(request):
    return render(request, "home_adsi.html")
