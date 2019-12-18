from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from django.shortcuts import redirect
# Create your views here.
def index(request):
    pass
    return render(request,'index.html')


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


def elements(request):
    return render(request,'elements.html')

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password= password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            context['error'] = "Provide valid credentials !!"
            return render(request, "login.html", context)
    else:
        return render(request, "login.html", context)


def user_logout(request):
    logout(request)
    return redirect('user_login')


def singleBlog(request):
    return render(request,'single-blog.html')

def singleProduct(request):
    return render(request,'single-product.html')

def tracking(request):
    return render(request,'tracking.html')