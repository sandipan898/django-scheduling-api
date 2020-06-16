from rest_framework import serializers
from .models import ScheduleCall


class ScheduleCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleCall
        timestamp = serializers.DateTimeField()
        fields = (
            'site_url', 'timestamp',
        )