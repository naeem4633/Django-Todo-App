from django.db import models

# Create your models here.

class Todo(models.Model):
    todo_title = models.CharField(max_length=200)
    todo_description = models.TextField(null=True)
    todo_status = models.CharField(max_length=100, default='In progress')

    def __str__(self):
        return self.todo_title