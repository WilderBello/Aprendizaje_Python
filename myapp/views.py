from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
# Create your views here.


def hello(request):
    return HttpResponse("<h1>Hello World</h1>")


def about(request):
    return render(request, "about.html")


def projects(request):
    projects = list(Project.objects.values())
    # return HttpResponse("projects")
    return JsonResponse(projects, safe=False)
    # return render('./templates/projects.html')


def tasks(request, id):
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    # return HttpResponse('tasks')
    return HttpResponse(f'task: {task.title}')
