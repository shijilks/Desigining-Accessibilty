from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','category',' Product_image']
