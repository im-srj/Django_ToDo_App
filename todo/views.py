from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def tasks(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks")

    form = TaskForm()
    tasks = Task.objects.all().order_by("priority")
    return render(request, "todo.html", {"form": form, "tasks": tasks})


def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("tasks")


def completed(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = True
    task.save()
    return redirect("tasks")


def clear(request):
    Task.objects.all().delete()
    return redirect("tasks")
