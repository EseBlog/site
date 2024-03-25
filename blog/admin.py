from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import General, Materia, Etiqueta, Post

# Register your models here.
@admin.register(General)
class GeneralAdmin(ImportExportModelAdmin):
    list_display= ['nombre','creacion', 'actualizacion']
    
@admin.register(Materia)
class MateriaAdmin(ImportExportModelAdmin):
    list_display= ['materia','creacion', 'actualizacion']

@admin.register(Etiqueta)
class EtiquetaAdmin(ImportExportModelAdmin):
    list_display= ['etiqueta','creacion', 'actualizacion']

@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    list_display= ['titulo','creacion', 'actualizacion', 'autor', 'materia']
