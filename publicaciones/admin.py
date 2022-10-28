from django.contrib import admin
from publicaciones.models import publicacion,categoria
from users.models import Profile,Country


@admin.register(publicacion)
class publicacionAdmin(admin.ModelAdmin):
    list_display = ['user','title','dt_creation','dt_update']

@admin.register(categoria)
class categoriaAdmin(admin.ModelAdmin):
    list_display = ['name','description','is_active']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name','surname','birthday']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']


