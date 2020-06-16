from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework import permissions
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response

from .serializers import ScheduleCallSerializer
from .models import ScheduleCall

# Create your views here.


class ScheduleCallView(viewsets.ModelViewSet):
    
    """ Creating and Listing ScheduleCall class objects.
        It will also retrieve object by getting parameters passed through the API call
    """

    serializer_class = ScheduleCallSerializer
    queryset = ScheduleCall.objects.all()

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['pk'])
        obj = ScheduleCall.objects.filter(id=params['pk'])
        print(obj)
        serializer = ScheduleCallSerializer(obj, many=True)
        return Response(serializer.data)
    
