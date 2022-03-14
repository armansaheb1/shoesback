from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Item, Material, Part, Pattern

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "id",
            "name",
            "get_pic",
            "pic"
        )
class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = (
            "id",
            "item",
            "name",
            "model",
            "get_model",
        )

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            "id",
            "part",
            "name",
            "shininess",
        )

class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = (
            "material",
            "name",
            "color",
            "texture",
        )