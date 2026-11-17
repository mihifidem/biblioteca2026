from django.contrib import admin

# Register your models here.
from .models import Libro, Genero

admin.site.register(Libro)  
admin.site.register(Genero)