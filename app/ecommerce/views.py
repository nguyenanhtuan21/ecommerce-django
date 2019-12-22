from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User

### import models 
from .models import Instagram

from django.shortcuts import redirect

from .forms import SignUpForm
# Create your views here.
@login_required(login_url='/login/')
def index(request):
    context = {}
    instagrams = Instagram.objects.all().order_by('-id')[:5]
    context['instagrams'] = instagrams
    return render(request,'index.html',context)


@login_required(login_url='/login/')
def about(request):
    return render(request,'about.html')


@login_required(login_url='/login/')
def blog(request):
    return render(request,'blog.html')


@login_required(login_url='/login/')
def cart(request):
    return render(request,'cart.html')

def category(request):
    return render(request,'category.html')
    
@login_required(login_url='/login/')
def checkout(request):
    return render(request,'checkout.html')

@login_required(login_url='/login/')
def confirmation(request):
    return render(request,'confirmation.html')

@login_required(login_url='/login/')
def contact(request):
    return render(request,'contact.html')




def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password= password)
        if user:
            login(request, user)
            # next = request.POST.get('next', '/')
            # print(next)
            return redirect('index')
        else:
            context['error'] = "Provide valid credentials !!"
            return render(request, "login.html", context)
    else:
        return render(request, "login.html", context)


def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required(login_url='/login/')
def singleBlog(request):
    return render(request,'single-blog.html')

def singleProduct(request):
    return render(request,'single-product.html')
@login_required(login_url='/login/')
def tracking(request):
    return render(request,'tracking.html')



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
