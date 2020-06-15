from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework import permissions
from rest_framework import generics, mixins

from .serializers import ScheduleCallSerializer
from .models import ScheduleCall

# Create your views here.


class ScheduleCallView(generics.ListCreateAPIView):
    serializer_class = ScheduleCallSerializer
    queryset = ScheduleCall.objects.all()
    
