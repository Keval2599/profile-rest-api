from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status
# Create your views here.


class HelloApiView(APIView):


    serializer_class = serializers.HelloSerializer
    def get(self, request,format=None):
        an_apiview = [
        'Uses HTTP method as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives You the most control over you applcation logic',
        'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk=None):
        return  Response({'method':'PUT'})
    def patch(self, request, pk=None):
        return Response({'methos' : 'PATCH'})
    def delete(self, request, pk=None):
        return Response({'method' : 'DELETE'})
