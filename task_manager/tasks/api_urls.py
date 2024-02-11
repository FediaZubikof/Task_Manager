from django.urls import path
from . import api_views

urlpatterns = [
    path('task/', api_views.Task_API.as_view(), name="api-task"),
    path('task/<int:pk>/', api_views.Task_API.as_view(), name="api-update-task"),
]