from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class categoria(models.Model):
    """
    Categorias
    """

    name = models.CharField(max_length=40, blank=False, null=False)
    description = models.TextField(null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class publicacion(models.Model):
    """
    Publication
    """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    title = models.CharField(max_length=40, blank=False, null=False)        
    content = models.TextField(null=False)
    category = models.ForeignKey(categoria,on_delete=models.RESTRICT)    
    dt_creation = models.DateTimeField(default=timezone.now)
    dt_update = models.DateTimeField(default=timezone.now)
    main_image = models.ImageField(upload_to='post_image', default='post_image/post-image-default-2.png', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'





 
