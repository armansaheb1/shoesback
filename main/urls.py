from django.contrib import admin
from django.urls import path, include
from rest_framework import views
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [

#  < ------------ General
    path('items' , views.items.as_view() , name='items'),
    path('item' , views.item.as_view() , name='item'),
    path('item/<int:id>' , views.item.as_view() , name='item'),
    path('category' , views.category.as_view() , name='category'),
    path('part' , views.part.as_view() , name='part'),
    path('part/<int:id>' , views.part.as_view() , name='part'),
    path('parts/<int:id>' , views.parts.as_view() , name='parts'),
    path('material' , views.material.as_view() , name='material'),
    path('material/<int:id>' , views.material.as_view() , name='material'),
    path('materials/<int:id>' , views.materials.as_view() , name='materials'),
    path('pattern' , views.pattern.as_view() , name='pattern'),
    path('pattern/<int:id>' , views.pattern.as_view() , name='pattern'),
    path('patterns/<int:id>' , views.patterns.as_view() , name='patterns'),
    path('itemparts/<int:id>' , views.itemparts.as_view() , name='itemparts'),
    path('pattern' , views.patterns.as_view() , name='pattern'),
    path('itemmaterials/<int:id>' , views.itemmaterials.as_view() , name='itemmaterials'),
    path('itemmaterial' , views.itemmaterials.as_view() , name='itemmaterials'),

] 