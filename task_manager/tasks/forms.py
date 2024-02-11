from django import forms
from .models import Task, Task_Img


# Переопределить dateinput и datetimeinput, чтобы django мог читать html-селекторы date и datetime.
class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control Roboto', 'placeholder': 'Название задачи'}),
        }
        labels = {
            'title': 'Добавьте название задачи',

        }


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'd_time']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control Roboto', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'custom-class', 'placeholder': 'Описание'}),
            'priority': forms.Select(attrs={'class': 'custom-class'}),
            'mark': forms.CheckboxInput(attrs={'class': 'custom-class'}),
            'd_time': DateTimeInput(attrs={'class': 'custom-class', 'placeholder': '%Y-%m-%d %H:%M:%S'}),

        }
        labels = {
            'title': 'Название задачи',
            'd_time': 'Время окончания',
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Task_Img
        fields = ['img']
