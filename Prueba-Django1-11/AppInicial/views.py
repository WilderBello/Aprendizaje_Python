from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def first_view(request):
    # return HttpResponse("Comentario")
    context = {
        'sample_var': 'ejemplo',
        'otra_cosa': [2, 4, 5]
    }
    return render(request, 'inicio.html', context)
