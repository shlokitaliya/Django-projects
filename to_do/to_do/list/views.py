from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'index.html')



@login_required
def task_list(request):
    # Fetch tasks for the logged-in user
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('list:task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

@login_required
def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed  # Toggle completion status
    task.save()
    return redirect('list:task_list')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'add_task.html', {'form': form})  # Reusing add_task template


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('list:task_list')