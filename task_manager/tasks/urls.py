from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.TaskListView.as_view()), name='tasks'),
    path('create_task/', login_required(views.TaskCreateView.as_view()), name='create_task'),
    path('more_details/<int:pk>/', login_required(views.TaskDetailsView.as_view()), name='more_details'),
    path('update_task/<int:pk>/', login_required(views.TaskUpdateView.as_view()), name='update_task'),
    path('delete/<int:pk>/', login_required(views.TaskDeleteView.as_view()), name='task_delete'),
    path('add_photo/<int:id>/', views.add_photo, name='add_photo'),
    path('delete_photo/<int:id>/', views.delete_photo, name='delete_photo'),
    path('complete/<int:id>/', views.complete, name='complete'),
    path('priority_filter/<str:priority>/', login_required(views.TaskListView.as_view()), name='priority_filter'),

]
