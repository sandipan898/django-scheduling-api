from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostArticleSerializer
from .models import PostArticle

# Create your views here.

@permission_classes((permissions.AllowAny,))
class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'status': 'OK',
        }
        return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = PostArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
