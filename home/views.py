from django.shortcuts import render
from rest_framework import APIView
from rest_framework import status
from .models import MenuItem
from .serializers import ItemSerializer

class MenuView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items , many = True)
        return Response(serializer.data , status =status.HTTP_200_OK)

