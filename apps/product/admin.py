from product.models import  Category, Product, Order
from django.contrib import admin

class MyProductAdmin(admin.ModelAdmin):
    list_display  = ('name', 'image_tag')
    
admin.site.register(Category)
admin.site.register(Product, MyProductAdmin)
admin.site.register(Order)