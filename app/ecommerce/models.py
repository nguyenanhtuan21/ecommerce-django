from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import timezone

# Create your models here.
SIZE = (
    ('S','S'),
    ('M','M'),
    ('L','L'),
    ('XL','XL'),
)

CATEGORY = (
    ('TR','TROUSERS'),
    ('S','SHIRT'),
    ('SH','SHOES'),
)
COLOR = (
    ('R','Red'),
    ('B','Blue'),
    ('BL','Black'),
    ('Y','Yellow'),
    ('W','White'),
)
CATEGORY_BLOG = (
    ('FOOD','FOOD'),
    ('PRODUCT','PRODUCT'),
    ('TRAVEL','TRAVEL'),
    ('HEALTHY','HEALTHY'),
)


class Brand(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField()
    pictute = models.ImageField(upload_to='Product/', height_field=None, width_field=None, max_length=None)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254,blank=True,null=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_at']

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(choices = CATEGORY, max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    size = models.CharField(choices = SIZE, max_length=20)
    color = models.CharField(max_length=50, choices = COLOR)
    image = models.ImageField(upload_to='Product/', height_field=None, width_field=None, max_length=None)
    quantity_in_stock = models.IntegerField()
    introduction = models.TextField(max_length=200,blank=True)
    description = models.TextField()
    coupon = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    def get_absolute_price(self):
        minus_price = (self.price*self.coupon)/100
        absolute_price = self.price - minus_price
        return absolute_price

    def get_category(self):
        return dict(CATEGORY)[self.category]
    def get_color(self):
        return dict(COLOR)[self.color]
    class Meta:
        ordering = ['-created_at']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Profile/', height_field=None, width_field=None, max_length=None)
    address = models.TextField(max_length=300)
    birthday = models.DateTimeField(blank=True, null=True)
    level = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username

class Instagram(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='Instagram/', height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_order = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.quantity + ' product: ' + self.product.name
    def get_total(self):
        return self.product.get_absolute_price*self.quantity

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderItem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username
    def get_price_total(self):
        total = 0
        for product in self.products.all():
            total += product.get_total()
        return total



class PostBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField( max_length=150)
    category = models.CharField(choices=CATEGORY_BLOG,max_length=50)
    introduction = models.CharField(max_length=200)
    content = models.TextField()
    image =  models.ImageField(upload_to='Blog/', height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class CommentBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostBlog, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

     


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()







    
    
    
    



    
    


