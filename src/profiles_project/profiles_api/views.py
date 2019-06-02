from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of API features"""

        an_apiview = ['A', 'B', 'C']

        return Response({'message':'Helo', 'APIView':an_apiview})