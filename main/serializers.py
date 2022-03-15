from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Item, ItemMaterials, Material, Part, Pattern

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "id",
            "name",
            "get_pic",
            "pic",
            "cat",
            "patina",
            "patinad"
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = (
            "id",
            "item",
            "name",
            "model",
            "default",
            "bumpmap", 
            "get_model",
        )

class ItemMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMaterials
        fields = (
            "part",
            "material",
        )
        
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            "id",
            "name",
            "repeat",
            "bumpmap"
        )

class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = (
            "id",
            "material",
            "shininess",
            "icon", 
            "name",
            "color",
            "texture",
            "get_material"
        )