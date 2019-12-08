from django.urls import path
from .views import (
    about,
    blog,
    cart,
    category,
    checkout,
    confirmation,
    contact,
    index,
    elements,
    login,
    singleBlog,
    singleProduct,
    tracking,
)
urlpatterns = [
    path('about/',about,name='about'),
    path('blog/',blog,name='blog'),
    path('cart/',cart,name='cart'),
    path('category/',category,name='category'),
    path('checkout/',checkout,name='checkout'),
    path('confirmation/',confirmation,name='confirmation'),
    path('contact/',contact,name='contact'),
    path('',index,name='index'),
    path('elements/',elements,name='elements'),
    path('login/',login,name='login'),
    path('single-blog',singleBlog,name='singleblog'),
    path('single-product/',singleProduct,name='single-product'),
    path('tracking/',tracking,name='tracking')
]
