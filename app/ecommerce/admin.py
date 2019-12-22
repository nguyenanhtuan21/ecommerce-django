from django.contrib import admin
from .models import Brand, Product, Profile, Instagram, OrderItem,Order
from django.utils.html import format_html
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = ['id','name','descriptions','address','phone','created_at','updated_at']
    list_filter = ['id','name','created_at','updated_at']
    search_fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','category','brand','price','size','color','quantity_in_stock','introduction','description','created_at','updated_at']
    list_filter = ['id','created_at','updated_at']
    search_fields = ['name']

class ProfileAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150px" height="150px" />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    list_display = ['id','user','image','address','birthday','created_at','updated_at']
    search_fields = ['user']
    list_filter = ['id','user','created_at','updated_at']
class InstaAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150px" height="150px" />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    list_display = ['id','name','image','image_tag']
    list_filter = ['id','name','created_at','updated_at']
    search_fields = ['name']
    

    
    
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['user','is_order','product','quantity','created_at','updated_at']
    list_filter = ['id','user','created_at','updated_at']
    search_fields = ['user']
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','created_at','updated_at']
    list_filter = ['user','created_at','updated_at']
    search_fields = ['user']

admin.site.register(Brand,BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Instagram,InstaAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Order,OrderAdmin)

