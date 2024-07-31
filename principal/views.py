from django.shortcuts import render

# Create your views here.


def home(request):
    projects = [
        {'id': 1, 'name': 'Atomatización de Procesos de Manufactura', 'url': 'proyecto_apm/', 'image_url': 'img/pexels-david-besh-884788.jpg'},
        {'id': 2, 'name': 'Robótica', 'url': 'proyecto_robotica/', 'image_url': 'img/pexels-david-besh-884788.jpg'}, 
        {'id': 3, 'name': 'Análisis y Desarrollo de Sistemas de Información', 'url': 'proyecto_adsi/', 'image_url': 'img/pexels-david-besh-884788.jpg'},
    ]
    return render(request, 'inicio.html', {'projects': projects})
    # return render(request, "index.html")