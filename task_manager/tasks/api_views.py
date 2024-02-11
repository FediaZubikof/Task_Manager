from django.shortcuts import render
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Task


# Create your views here.
class Task_API(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            task = Task.objects.get(id=id)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        else:
            task = Task.objects.all()
            serializer = TaskSerializer(task, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Созданные данные'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        id = pk
        task_id = Task.objects.get(pk=id)
        serializer = TaskSerializer(task_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Обновлены полные данные'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        id = pk
        task_id = Task.objects.get(pk=id)
        serializer = TaskSerializer(task_id, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Обновлены частичные данные'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        id = pk
        task = Task.objects.get(pk=id)
        task.delete()
        return Response({'msg': 'Обновленные данные'})
