# main/urls.py
from django.urls import path

from .views import clear_completed, delete_task, home, list_delete, list_detail, list_edit, toggle_task

urlpatterns = [
    path('', home, name='home'),
    path('list/<int:list_id>/', list_detail, name='list-detail'),
    path('list/<int:list_id>/edit/', list_edit, name='list-edit'),
    path('list/<int:list_id>/delete/', list_delete, name='list-delete'),
    path('list/<int:list_id>/task/<int:task_id>/toggle/', toggle_task, name='task-toggle'),
    path('list/<int:list_id>/task/<int:task_id>/delete/', delete_task, name='task-delete'),
    path('list/<int:list_id>/tasks/clear-completed/', clear_completed, name='tasks-clear-completed'),
]