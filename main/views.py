from django.shortcuts import render
from .serializers import ItemSerializer, MaterialSerializer, PartSerializer, PatternSerializer
from .models import Item, ItemMaterials, Material , Part, Pattern
from django.http import HttpResponse , Http404 
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import authentication
# Create your views here.


class items(APIView):

    def get_object(self):
        try:
            return Item.objects.all()
        except Item.DoesNotExist:
            return Http404
            
    def get(self , request , format = None):
        query = self.get_object()
        serializer = ItemSerializer(query , many=True)
        return Response(serializer.data)
    
    def post(self , request , format = None):
        query = Item.objects.filter(id = request.data['id'])
        serializer = ItemSerializer(query , many=True)
        return Response(serializer.data)

class item(APIView):
#    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
#    permission_classes = [IsAuthenticated]

    def get_object(self , id):
        try:
            return 
        except Item.DoesNotExist:
            return Http404

    def put(self , request , id , format = None):
        query = Item.objects.get(id)
        serializer = ItemSerializer(query[0],  data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self , request, id , format = None):
        query = Item.objects.get(id)
        query[0].delete()

    def post(self , request , format = None):
        serializer = ItemSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class part(APIView):

    def post(self , request , format = None):
        serializer = PartSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status= status.HTTP_404_NOT_FOUND)

    def put(self , request , id , format = None):
        query = Part.objects.get(id)
        serializer = PartSerializer(query[0],  data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self , request, id , format = None):
        query = Part.objects.get(id)
        query[0].delete()
        
class parts(APIView):

    def get_object(self , id):
        try:
            return Part.objects.filter(item = id)
        except Part.DoesNotExist:
            return Http404
            
    def get(self , request , id , format = None):
        query = self.get_object(id)
        serializer = PartSerializer(query , many=True)
        return Response(serializer.data)

class material(APIView):

    def post(self , request , format = None):
        serializer = MaterialSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status= status.HTTP_404_NOT_FOUND)

    def put(self , request , id , format = None):
        query = Material.objects.get(id)
        serializer = MaterialSerializer(query[0],  data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self , request, id , format = None):
        query = Material.objects.get(id)
        query[0].delete()

class materials(APIView):

    def get_object(self , id):
        try:
            return Material.objects.filter(part = id)
        except Material.DoesNotExist:
            return Http404
            
    def get(self , request , id , format = None):
        query = self.get_object(id)
        serializer = MaterialSerializer(query , many=True)
        return Response(serializer.data)


class pattern(APIView):

    def post(self , request , format = None):
        serializer = PatternSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors,status= status.HTTP_404_NOT_FOUND)

    def put(self , request , id , format = None):
        query = Pattern.objects.get(id)
        serializer = PatternSerializer(query[0],  data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self , request, id , format = None):
        query = Pattern.objects.get(id)
        query[0].delete()

class patterns(APIView):

    def get_object(self , id):
        try:
            return Pattern.objects.filter(material = id)
        except Pattern.DoesNotExist:
            return Http404
            
    def get(self , request , id , format = None):
        query = self.get_object(id)
        serializer = PatternSerializer(query , many=True)
        return Response(serializer.data)

class itemparts(APIView):

    def get_object(self , id):
        try:
            return Part.objects.filter(item = Item.objects.get(id = id))
        except Part.DoesNotExist:
            return Http404
            
    def get(self , request , id , format = None):
        query = self.get_object(id)
        serializer = PartSerializer(query , many=True)
        return Response(serializer.data)

class itemmaterials(APIView):
            
    def get(self , request , id , format = None):
        parts = Part.objects.filter(item = Item.objects.get(id = id))
        partslist = []
        materialslist = []
        patternslist  = {}
        for item in parts :
            materials = ItemMaterials.objects.get(part = item).material.all()
            materialslist = []
            for itemm in materials:
                patterns = Pattern.objects.filter(material = itemm)
                patternslist  = {}
                for itemmm in patterns:
                    if itemmm.type == 'color':
                        patternslist[itemmm.name] = {'code': itemmm.color , 'shininess' : itemm.shininess}
                    else:
                        patternslist[itemmm.name] = {'pic': itemmm.get_pic() , 'shininess' : itemm.shininess}
                materialslist.append({'name' :  itemm.name , 'pic': itemm.get_map() , 'colors': patternslist})
            partslist.append({'name': item.name , 'bump': materialslist})
        print(partslist)
        return Response(partslist)