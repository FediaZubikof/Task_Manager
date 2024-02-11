from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'c_time', 'u_time', 'd_time', 'priority', 'mark']

    # def get_formatted_d_time(self, obj):
    #     return obj.d_time.strftime('%Y-%m-%d %H:%M:%S')
