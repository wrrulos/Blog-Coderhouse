from django.shortcuts import render
from publicaciones.models import publicacion
from django.utils import timezone

def index(request):      
    publicaciones = publicacion.objects.all().order_by('-dt_update')
    context = {'publicaciones': publicaciones}    
    return render(request,'index.html',context = context)

def about(request):
    return render(request,'about.html',context = {})

    
