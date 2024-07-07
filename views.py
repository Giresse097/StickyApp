from django.shortcuts import render, get_object_or_404, redirect
from .models import Task


def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status') == 'true'
        priority = request.POST.get('priority')
        Task.objects.create(title=title,
                            description=description,
                            due_date=due_date, status=status,
                            priority=priority)
        return redirect('home_page')
    return render(request, 'create_task.html')


def home_page(request):
    tasks = Task.objects.all()
    return render(request, 'home_page.html', {'tasks': tasks})


def read_task(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'read_task.html', {'task': task})


def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.priority = request.POST.get('priority')
        task.save()
        return redirect('home_page')
    return render(request, 'update_task.html', {'tasks': task})


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect('home_page')
    return render(request, 'delete_task.html', {'tasks': task})
