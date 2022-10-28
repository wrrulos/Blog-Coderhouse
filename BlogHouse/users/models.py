from tabnanny import verbose
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.name

    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=48,default='-')
    surname = models.CharField(max_length=64,default='-')                            
    birthday = models.DateField(default = timezone.now)    
    country = models.ForeignKey(Country,on_delete=models.RESTRICT)
    img_profile = models.ImageField(upload_to = 'profile_images',default='profile_images/default-user.jpg',blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        


   
