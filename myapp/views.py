from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from .models import Item
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def index(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)