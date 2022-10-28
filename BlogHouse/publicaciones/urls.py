from django.contrib import admin
from django.urls import path,include
from Bloggerhouse.views import index
from publicaciones.views import create_publicacion,detail_publicaciones,delete_publicacion_view,update_publicacion_view,search_publicacion_view

urlpatterns = [    
path('create-post/', create_publicacion, name='create_publicacion'),
path('detail-post/<int:pk>/', detail_publicaciones, name='detail_publicaciones'),
path('delete-post/<int:pk>/', delete_publicacion_view, name='delete_publicacion'),
path('update-post/<int:pk>/', update_publicacion_view, name='update_publicacion'),
path('search-post/', search_publicacion_view, name='search_publicacion_view'),
] 