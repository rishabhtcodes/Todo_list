from django.db import models

class ToDoList(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Task(models.Model):
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='tasks')
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description