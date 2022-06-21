from django.contrib import admin
from .models import *


class CursoAdmin(admin.ModelAdmin):

    list_display = ('name','profesor','duration', 'price')
    search_fields = ('name', 'profesor') 

admin.site.register(Curso,CursoAdmin)

class EventoAdmin(admin.ModelAdmin):

    list_display = ('name','city','date')
    search_fields = ('name', 'city') 

admin.site.register(Evento,EventoAdmin)

# Register your models here.
