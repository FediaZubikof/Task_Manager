from django.shortcuts import render, redirect
from django.views import View
from .models import Task, Task_Img
from .forms import TaskForm, TaskUpdateForm, PhotoForm
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse


class TaskListView(View):
    template_name = 'tasks/tasks.html'

    def get(self, request, priority=None):
        if priority is None:
            tasks = Task.objects.all().filter(user=request.user).order_by('-id')
            bgall = 'primary'
            bgh = None
            bgm = None
            bgl = None

        elif priority == 'High':
            tasks = Task.objects.all().filter(user=request.user, priority='High').order_by('-id')
            bgall = None
            bgh = 'primary'
            bgm = None
            bgl = None
        elif priority == 'Medium':
            tasks = Task.objects.all().filter(user=request.user, priority='Medium').order_by('-id')
            bgall = None
            bgh = None
            bgm = 'primary'
            bgl = None
        else:
            tasks = Task.objects.all().filter(user=request.user, priority='Low').order_by('-id')
            bgall = None
            bgh = None
            bgm = None
            bgl = 'primary'

        form = TaskForm()
        context = {'task_list': tasks, 'form': form, 'bgall': bgall, 'bgh': bgh, 'bgm': bgm, 'bgl': bgl}

        return render(request, self.template_name, context)


class TaskDetailsView(View):
    template_name = 'tasks/task_details.html'

    def get(self, request, pk):
        try:
            tasks = Task.objects.get(pk=pk, user=request.user)
            task_img = Task_Img.objects.all().filter(task=pk)
            context = {'task': tasks, 'task_img': task_img}
        except Task.DoesNotExist:
            return redirect('/')

        return render(request, self.template_name, context)


class TaskCreateView(CreateView):
    # указываем модель, которую хотим использовать
    model = Task
    form_class = TaskForm

    success_url = "/"

    template_name = 'tasks/tasks.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Установите для пользователя значение текущего пользователя, вошедшего в систему
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    # указываем модель, которую хотим использовать
    model = Task
    form_class = TaskUpdateForm

    def get_success_url(self):
        # Redirect to the 'more_details' URL with the primary key (ID) of the created object
        return reverse('more_details', args=[self.object.pk])

    template_name = 'tasks/task_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Установите для пользователя значение текущего пользователя, вошедшего в систему
        return super().form_valid(form)


class TaskDeleteView(DeleteView):
    # указываем модель, которую хотим использовать
    model = Task

    # можно указать URL успешного выполнения
    # url для перенаправления после успешного выполнения
    # удаление объекта
    success_url = "/"

    template_name = 'tasks/tasks.html'


def add_photo(request, id):
    if request.method == 'POST':

        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            task = Task.objects.get(pk=id)
            img = form.cleaned_data['img']
            img_form = Task_Img(task=task, img=img)
            img_form.save()
            return redirect(f'/more_details/{id}/')  # Перенаправить на просмотр, отображающий список скриншотов
    else:
        form = PhotoForm()

    context = {'form': form}

    return render(request, 'tasks/add_photo.html', context)


def delete_photo(request, id):
    if request.method == 'POST':
        task_id = Task_Img.objects.get(pk=id).task.id

        pi = Task_Img.objects.get(pk=id)
        pi.delete()
        return redirect(f'/more_details/{task_id}/')

    return render(request, 'tasks/task_details.html')


def complete(request, id):
    if request.method == 'POST':
        task = Task.objects.get(pk=id)
        if task.mark:
            task.mark = False
            task.save()

            return redirect('/')
        else:
            task.mark = True
            task.save()
            return redirect('/')
    return render(request, 'tasks/tasks.html')
