from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.
class HelloAPIView(APIView):
    """Hello world for APIView testing"""

    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = ['get', 'post', 'patch', 'put', 'delete']
        return Response({'message': 'Hello', 'APi_list': an_apiview})

    def post(self, request):
        """Post request with name"""
        serializer = self.serializers_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = 'Hello ' + name
            return Response({'messgae': msg})
        else:
            return Response(serializer.errors,
                            status.HTTP_400_BAD_REQUEST
                    )