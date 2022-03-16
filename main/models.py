from base64 import encode
from timeit import repeat
from unicodedata import name
from django.db import models
from shoes.settings import ROOT, SECRET_KEY

# Create your models here.

    
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to = 'items')
    cat = models.ForeignKey(Category , related_name = 'category' , on_delete=models.CASCADE)
    patina = models.BooleanField(default=False)
    patinad = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    def get_pic(self):
        return f'{ROOT}/media/{self.pic}'



class Material(models.Model):
    name = models.CharField(max_length=100)
    repeat = models.IntegerField()
    bumpmap = models.ImageField(upload_to = 'bumpmaps' , null=True , blank =True)
    def __str__(self):
        return self.name
    def get_map(self):
        return f'{ROOT}/media/{self.bumpmap}'

class Pattern(models.Model):
    material = models.ForeignKey(Material , related_name='patterns' , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    icon = models.ImageField(upload_to = 'textures' , blank=True, null= True)
    color = models.CharField(max_length= 20 , blank=True , null=True)
    shininess = models.FloatField(default= 300)
    texture = models.ImageField(upload_to = 'textures' , blank=True, null= True)
    def __str__(self):
        return self.name + '-' + self.material.name + '-'
    def get_pic(self):
        if self.texture:
            return f'{ROOT}/media/{self.texture}'
        else:
            return False
    def get_icon(self):
        if self.icon:
            return f'{ROOT}/media/{self.icon}'
        else:
            return False
    def get_color(self):
        if self.color:
            return self.color
        else:
            return False
    def get_material(self):
        return self.material.name


class Part(models.Model):
    item = models.ForeignKey(Item , related_name = 'parts' , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    model = models.FileField(upload_to='models' , null=True)
    default = models.ForeignKey(Pattern , related_name = 'category' , on_delete=models.CASCADE)
    bumpmap = models.ImageField(upload_to = 'textures' , blank=True, null= True)
    def __str__(self):
        return self.name + '-' + self.item.name
    def get_model(self):
        return f'{ROOT}/media/{self.model}'
    def get_map(self):
        if self.bumpmap:
            return f'{ROOT}/media/{self.bumpmap}'


class ItemMaterials(models.Model):
    part = models.ForeignKey(Part , on_delete=models.CASCADE)
    material = models.ManyToManyField(Material)
    def __str__(self):
        return self.part.name + '-' + self.part.item.name