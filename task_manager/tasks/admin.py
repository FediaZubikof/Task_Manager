from django.contrib import admin
from .models import Task, Task_Img


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'description', 'c_time', 'u_time', 'd_time', 'priority']


admin.site.register(Task, TaskAdmin)


class TaskImgAdmin(admin.ModelAdmin):
    list_display = ['id', 'task_id', 'task_title', 'img']

    @admin.display(ordering="task__title")
    def task_title(self, obj):
        return obj.task.title

    @admin.display(ordering="task__id")
    def task_id(self, obj):
        return obj.task.id


admin.site.register(Task_Img, TaskImgAdmin)
