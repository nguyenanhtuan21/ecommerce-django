from django.contrib import admin
from .models import Brand, Product, Profile, Instagram, OrderItem,Order

# Register your models here.


admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Instagram)
admin.site.register(OrderItem)
admin.site.register(Order)

