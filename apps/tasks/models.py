from django.db import models
from django.conf import settings
from apps.projects.models import Project


class Task(models.Model):

    class Status(models.TextChoices):
        TODO = "TODO", "To Do"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        DONE = "DONE", "Done"

    class Priority(models.TextChoices):
        LOW = "LOW", "Low"
        MEDIUM = "MEDIUM", "Medium"
        HIGH = "HIGH", "High"

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    project = models.ForeignKey( Project, on_delete=models.CASCADE, related_name="tasks")

    assignee = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="assigned_tasks")

    status = models.CharField(max_length=20,choices=Status.choices,default=Status.TODO)

    priority = models.CharField(max_length=20,choices=Priority.choices,default=Priority.MEDIUM)

    due_date = models.DateField( null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.title
