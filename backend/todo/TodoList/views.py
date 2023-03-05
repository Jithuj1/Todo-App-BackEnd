from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TodoSerializer
from .models import Today
# Create your views here.


@api_view(['GET', 'POST'])
def Home(request):
    if request.method == "GET":
        day = Today.objects.all()
        serializer = TodoSerializer(day, many = True)
        return Response (serializer.data)
    else:
        print(request.data)
        serializer = TodoSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"status":status.HTTP_403_FORBIDDEN})
        

@api_view(['GET', 'PUT', 'DELETE'])
def Delete(request, id):
    try:
        todo = Today.objects.get(id=id)
        print(todo)
    except todo.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        todo = Today.objects.get(id = id)
        if todo:
            todo.delete()
            return Response ("Deleted")
        else:
            return Response (status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = TodoSerializer(todo, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors, Status = 400)