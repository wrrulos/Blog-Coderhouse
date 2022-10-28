from django.contrib import admin
from django.urls import path,include
from Bloggerhouse.views import index
from users.views import login_view,logout_view,register_view,profile_view

urlpatterns = [    
path('login/', login_view, name='login'),
path('logout/', logout_view, name='logout'), 
path('register/', register_view, name='register'),
path('profile/', profile_view, name='profile')
] 