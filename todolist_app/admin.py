from django.contrib import admin
from .models import TaskList, TaskItem

# Register your models here.
admin.site.register(TaskList)
admin.site.register(TaskItem)