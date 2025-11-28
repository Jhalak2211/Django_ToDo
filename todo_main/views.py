from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(iscompleted=False).order_by('-updated_at')
    
    completed_tasks = Task.objects.filter(iscompleted=True)
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'home.html', context)   