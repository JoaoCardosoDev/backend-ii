from django.contrib import admin

from todo.models import Task

# Register your models here.

@admin.tegister(Task)
class TaskAdmin(admin.ModelAdmin):
    pass