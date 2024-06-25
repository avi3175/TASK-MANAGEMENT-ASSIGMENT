from django.db import models
from django.utils import timezone
# Create your models here.


class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.taskTitle
