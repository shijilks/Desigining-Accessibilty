from django.contrib import admin
from .models import Product, Contact,Customer
# Register your models here.

admin.site.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','category',' Product_image']

admin.site.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')

admin.site.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','localiy','city','state','zipcode']