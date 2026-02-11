from django import forms

from .models import Task, ToDoList


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description']