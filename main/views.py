from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm, ToDoListForm
from .models import Task, ToDoList


def home(request):
    lists = ToDoList.objects.order_by('id')

    if request.method == 'POST':
        form = ToDoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ToDoListForm()

    return render(request, 'home.html', {'lists': lists, 'form': form})


def list_detail(request, list_id):
    todo_list = get_object_or_404(ToDoList, id=list_id)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.todo_list = todo_list
            task.save()
            return redirect('list-detail', list_id=todo_list.id)
    else:
        form = TaskForm()

    return render(request, 'todo_list.html', {'list': todo_list, 'form': form})


def list_edit(request, list_id):
    todo_list = get_object_or_404(ToDoList, id=list_id)

    if request.method == 'POST':
        form = ToDoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ToDoListForm(instance=todo_list)

    return render(request, 'list_edit.html', {'list': todo_list, 'form': form})


def list_delete(request, list_id):
    if request.method != 'POST':
        return redirect('home')

    todo_list = get_object_or_404(ToDoList, id=list_id)
    todo_list.delete()
    return redirect('home')


def toggle_task(request, list_id, task_id):
    if request.method != 'POST':
        return redirect('list-detail', list_id=list_id)

    task = get_object_or_404(Task, id=task_id, todo_list_id=list_id)
    task.completed = not task.completed
    task.save(update_fields=['completed'])
    if request.POST.get('next') == 'home':
        return redirect('home')
    return redirect('list-detail', list_id=list_id)


def delete_task(request, list_id, task_id):
    if request.method != 'POST':
        return redirect('list-detail', list_id=list_id)

    task = get_object_or_404(Task, id=task_id, todo_list_id=list_id)
    task.delete()
    if request.POST.get('next') == 'home':
        return redirect('home')
    return redirect('list-detail', list_id=list_id)


def clear_completed(request, list_id):
    if request.method != 'POST':
        return redirect('list-detail', list_id=list_id)

    Task.objects.filter(todo_list_id=list_id, completed=True).delete()
    if request.POST.get('next') == 'home':
        return redirect('home')
    return redirect('list-detail', list_id=list_id)