from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def cart(request):
    return render(request,'cart.html')

def category(request):
    return render(request,'category.html')

def checkout(request):
    return render(request,'checkout.html')

def confirmation(request):
    return render(request,'confirmation.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')

def elements(request):
    return render(request,'elements.html')

def login(request):
    return render(request,'login.html')

def singleBlog(request):
    return render(request,'single-blog.html')

def singleProduct(request):
    return render(request,'single-product.html')

def tracking(request):
    return render(request,'tracking.html')