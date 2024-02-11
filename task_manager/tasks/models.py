from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Низкий", "Низкий"),
        ("Средний", "Средний"),
        ("Высокий", "Высокий"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=100, null=True, verbose_name='Название задачи')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='Описание задачи')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    u_time = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    d_time = models.DateTimeField(null=True, blank=True, verbose_name='Время окончания')

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        null=True,
        blank=True,
        verbose_name='Уровень приоритета'
    )
    mark = models.BooleanField(default=False)


class Task_Img(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="task_img")
