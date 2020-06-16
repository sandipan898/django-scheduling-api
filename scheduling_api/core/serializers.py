from rest_framework import serializers
from .models import ScheduleCall


class ScheduleCallSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScheduleCall
        fields = '__all__'