from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "project",
        "assignee",
        "status",
        "priority",
        "due_date",
    )

    search_fields = (
        "title",
    )

    list_filter = (
        "status",
        "priority",
    )