from django.views.generic import DetailView
from django.shortcuts import redirect

from .models import ToDoList

class ToDoListDetailView(DetailView):
    model = ToDoList
    template_name = 'todo_list.html'   
    context_object_name = 'list'