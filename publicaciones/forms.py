from django import forms
from publicaciones.models import publicacion
from django.utils import timezone

class Publicacion_form(forms.ModelForm):
    
    dt_update = forms.DateTimeField(widget=forms.HiddenInput,initial = timezone.now)
    
    class Meta:
        model = publicacion
        fields = ['title','category','main_image','content']