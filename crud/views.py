import imp
from django.shortcuts import render
from rest_framework import viewsets
from .models import Ropa
from .serializers import RopaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, JSONParser

class Home(viewsets.ViewSet):

    parser_classes = (MultiPartParser,JSONParser)

    def list(self,request):
        lista = Ropa.objects.all()
        
        return Response({'data':RopaSerializer(lista,many=True).data},status = status.HTTP_200_OK)
    
    def create(self,request):
        object_to_create = RopaSerializer(data=request.data)
        if object_to_create.is_valid():
            object_to_create.save()
            return Response({'data':object_to_create.data},status = status.HTTP_201_CREATED)
        return Response({'data':object_to_create.errors})
        
    def update(self,request,pk=None):
        lista = Ropa.objects.filter(pk=pk).first()
        update = RopaSerializer(lista,request.data)
        if update.is_valid():
            update.save()
            return Response({'data':update.data},status = status.HTTP_200_OK)
        return Response({'data':update.errors})

    def delete(self,request,pk=None):
        lista = Ropa.objects.filter(pk=pk).first()
        if lista:
            lista.delete()
            return Response({'data':'eliminado'},status = status.HTTP_200_OK)
        return Response({'data':'eliminado'},status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        lista = Ropa.objects.filter(pk=pk).first()
        return Response({'data':RopaSerializer(lista).data},status = status.HTTP_200_OK)