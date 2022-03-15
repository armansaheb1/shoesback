from email.policy import default
from pickle import TRUE
from django.shortcuts import render
from .serializers import CategorySerializer, ItemMaterialsSerializer, ItemSerializer, MaterialSerializer, PartSerializer, PatternSerializer
from .models import Category, Item, ItemMaterials, Material , Part, Pattern
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
            return Item.objects.filter(id = id)
        except Item.DoesNotExist:
            return Http404

    def get(self , request , id , format = None):
        query = self.get_object(id)
        serializer = ItemSerializer(query , many=True)
        return Response(serializer.data)

    def put(self , request , id , format = None):
        query = Item.objects.get(id = id)
        serializer = ItemSerializer(query,  data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self , request, id , format = None):
        query = Item.objects.get(id = id)
        query.delete()
        return Response(status=status.HTTP_201_CREATED)

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
            query = Part.objects.filter(item = Item.objects.get(id = request.data['item']))
            serializer = PartSerializer(query , many = True)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(status= status.HTTP_404_NOT_FOUND)

    def put(self , request , id , format = None):
        query = Part.objects.get(id = id)
        serializer = PartSerializer(query,  data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self , request, id , format = None):
        query = Part.objects.get(id = id)
        query.delete()
        return Response(status=status.HTTP_201_CREATED)
        
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

    def get_object(self):
        try:
            return Material.objects.all()
        except Material.DoesNotExist:
            return Http404
            
    def get(self , request , format = None):
        query = self.get_object()
        serializer = MaterialSerializer(query , many=True)
        return Response(serializer.data)

    def post(self , request , format = None):
        serializer = MaterialSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status= status.HTTP_404_NOT_FOUND)

    def put(self , request , id , format = None):
        query = Material.objects.get(id = id)
        serializer = MaterialSerializer(query,  data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self , request, id , format = None):
        query = Material.objects.get(id = id)
        query.delete()
        return Response(status=status.HTTP_201_CREATED)

class materials(APIView):

    def get_object(self , id):
        try:
            return Material.objects.filter(id = id)
        except Material.DoesNotExist:
            return Http404
            
    def get(self , request , id , format = None):
        query = self.get_object(id)
        serializer = MaterialSerializer(query , many=True)
        return Response(serializer.data)



class pattern(APIView):


    def get_object(self):
        try:
            return Pattern.objects.all()
        except Pattern.DoesNotExist:
            return Http404
            
    def get(self , request , format = None):
        query = self.get_object()
        serializer = PatternSerializer(query , many=True)
        return Response(serializer.data)



    def post(self , request , format = None):
        serializer = PatternSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors,status= status.HTTP_404_NOT_FOUND)

    def put(self , request , id , format = None):
        query = Pattern.objects.get(id = id)
        serializer = PatternSerializer(query,  data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self , request, id , format = None):
        query = Pattern.objects.get(id = id)
        query.delete()
        return Response(status=status.HTTP_201_CREATED)

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

class category(APIView):

    def get_object(self):
        try:
            return Category.objects.all()
        except Part.DoesNotExist:
            return Http404
            
    def get(self , request , format = None):
        query = self.get_object()
        serializer = CategorySerializer(query , many=True)
        return Response(serializer.data)

    def post(self , request , format = None):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_404_NOT_FOUND)

class itemmaterials(APIView):
            
    def get(self , request , id , format = None):
        mainitem = Item.objects.get(id = id)
        parts = Part.objects.filter(item = mainitem)
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
                        patternslist[itemmm.name] = {'code': itemmm.get_color(), 'icon': itemmm.get_icon(), 'pic': itemmm.get_pic() , 'shininess' : itemmm.shininess}
                materialslist.append({'name' :  itemm.name , 'pic': itemm.get_map() , 'colors': patternslist})
                defa = {'code': item.default.get_color(), 'icon': itemmm.get_icon(), 'pic': item.default.get_pic()  , 'shininess' : item.default.shininess}
            partslist.append({'name': item.name , 'bump': materialslist , 'model': item.get_model() , 'default' : defa , 'patina': mainitem.patina, 'patinad': mainitem.patinad ,'bumpmap': item.get_map()})
        print(partslist)
        return Response(partslist)

    def post(self , request , format = None):
        serializer = ItemMaterialsSerializer(data = request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors,status= status.HTTP_404_NOT_FOUND)
    def put(self , request , format = None):
        query = ItemMaterials.objects.get(part = request.data['part'])
        