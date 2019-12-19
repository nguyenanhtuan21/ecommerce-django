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
    user_login,
    singleBlog,
    singleProduct,
    tracking,
    user_logout,
    register,
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
    path('login/',user_login,name='user_login'),
    path('single-blog',singleBlog,name='singleblog'),
    path('single-product/',singleProduct,name='single-product'),
    path('tracking/',tracking,name='tracking'),
    path('logout/',user_logout,name='user_logout'),
    path('register/',register,name='register')

]
