from django.contrib import admin

from .models import Popper
from .models import Candle
from .models import Balloon
from .models import Knife_Caketag
from .models import Prop_Decoration
from .models import Crown
from .models import Cap
from .models import New_Arrival





# Register your models here.
@admin.register(Popper)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title']
@admin.register(Candle)    
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title']
@admin.register(Balloon)    
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title']
@admin.register(Knife_Caketag)    
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title']
@admin.register(Prop_Decoration)    
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title']
@admin.register(Crown)    
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title']
@admin.register(Cap)    
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title']
@admin.register(New_Arrival)    
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title']
