from django.contrib import admin
from conteudo.models import comentarios

# Register your models here.

class AdminComentarios(admin.ModelAdmin):
    pass

admin.site.register(comentarios,AdminComentarios)