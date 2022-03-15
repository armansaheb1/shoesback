from django.contrib import admin

from main.models import Category, Item, ItemMaterials, Material, Part, Pattern

# Register your models here.
admin.site.register(Item)
admin.site.register(Part)
admin.site.register(Material)
admin.site.register(Pattern)
admin.site.register(ItemMaterials)
admin.site.register(Category)