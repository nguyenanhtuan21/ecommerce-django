from django.db import models

# Create your models here.
SIZE = (
    ('S','S'),
    ('M','M'),
    ('L','L'),
    ('XL','XL'),
)

CATEGORY = (
    ('TR','TROUSERS'),
    ('SH','SHIRT'),
    ('S','SHOES'),
)


# class Category(models.Model):
#     name = models.CharField(max_length=200)
#     descriptions = models.TextField()
#     pictute = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
#     active = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         ordering = ['-created_at']

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(choices = CATEGORY, max_length=50)
    
    


