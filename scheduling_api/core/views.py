import datetime
from django.shortcuts import render,redirect
from django.http import JsonResponse

# third party imports
from rest_framework import permissions
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ScheduleCallSerializer
from .models import ScheduleCall
generics.GenericAPIView
# Create your views here.


class ScheduleCallView(viewsets.ModelViewSet):
    
    """ Creating and Listing ScheduleCall class objects.
        It will also retrieve object by getting parameters passed through the API call
    """

    serializer_class = ScheduleCallSerializer

    def get_queryset(self, *args, **kwargs):
        qs = ScheduleCall.objects.all()
        for obj in qs:
            print(obj)
            print(datetime.datetime.now(), obj.timestamp)
            if datetime.datetime.now() == obj.timestamp:
                return redirect(obj.site_url)

        return ScheduleCall.objects.all()

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params)
        try: 
            params_list = params['pk'].split('-')
            obj = ScheduleCall.objects.filter(timestamp=params_list[0], site_url=params_list[1])
        except Exception as e:
            obj = ScheduleCall.objects.filter(site_url=params)
        print(obj)
        serializer = ScheduleCallSerializer(obj, many=True)
        return Response(serializer.data)
    



class ServerStateView(APIView):

    """To send response to the endpoint '/ping' which return a response of 'status': 'OK' to make sure that the server is alive"""
    
    def get(self, request, *args, **kwargs):
        state = {"status":"OK"}
        return Response(state)