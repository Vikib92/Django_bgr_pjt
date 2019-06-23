from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloAPIView(APIView):
    """Hello world for APIView testing"""

    def get(self, request, format=None):
        an_apiview = ['get', 'post', 'patch', 'put', 'delete']
        return Response({'message': 'Hello', 'APi_list': an_apiview})

