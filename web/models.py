# from django.db import models

# Create your models here.

from django.db import models
from django.contrib import admin
from search_admin_autocomplete.admin import SearchAutoCompleteAdmin
import uuid

from .choices import sexos, estado

# Create your models here.

# PLANTILLA PARA A GALERIA EN HOME
class Galeria (models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo          = models.CharField(max_length = 200, blank = False, null = False)    
    img             = models.ImageField(upload_to='galeria/')
    order           = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galerias'
        ordering = ['order']

    def _str_(self):
        return self.titulo
    
class GaleriaAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields   = ['titulo']
    list_display    =('titulo', 'order')
    list_per_page   = 10 # No of records per page


# PLANTILLA PARA LOS LINKS EN HOME
class Links (models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo          = models.CharField(max_length=200, blank= False, null = False)
    parrafo         = models.TextField()
    img             = models.ImageField(upload_to='links/')
    order           = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
        ordering = ['order']

    def _str_(self):
        return self.titulo

class LinksAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields   = ['titulo']
    list_display    =('titulo', 'order')
    list_per_page   = 10 # No of records per page

# CONTENIDO PRINCIPAL DE HISTORIA, NOTICIAS, ETC
class Front (models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    img             = models.ImageField(upload_to='front/')
    titulo          = models.CharField(max_length=200, blank=False, null=False)
    contenido       = models.TextField()
    order           = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Front'
        verbose_name_plural = 'Fronts'
        ordering = ['order']

    def _str_(self):
        return self.titulo

class FrontAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields   = ['titulo']
    list_display    = ('titulo', 'order')
    list_per_page   = 10


# CLASIFICA A QUE PERTENECEN LAS LISTAS DE IMAGENES DEL MODELO 'LISTA'
class Tipo (models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo            = models.CharField(max_length=200, blank=False, null= False, verbose_name="Tipo")
    descripcion     = models.TextField()
    order           = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['order']

    def _str_(self):
        return self.tipo
    
class TiposAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields   = ['tipo']
    list_display    = ('tipo', 'order')
    list_per_page   = 10


# ADMINISTRA EL LISTADO DE IMAGENES DE PRESIDENTES, COMITE, ETC...
class Listado (models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo            = models.ForeignKey(Tipo, blank=True, null=True, on_delete=models.CASCADE, verbose_name='tipo')
    titulo          = models.CharField(max_length=200, blank= False, null = False)
    img             = models.ImageField(upload_to='listado/')
    order           = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Listado'
        verbose_name_plural = 'Listados'
        ordering = ['order']

    def _str_(self):
        return self.titulo    

class ListadosAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields   = ['titulo']
    list_display    =('titulo', 'order')
    list_per_page   = 10 # No of records per page


# ADMINISTRA LOS CARDS DE TORNEO
class Card (models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo          = models.CharField(max_length=200, blank=False, null= False, verbose_name="Titulo")
    direccion       = models.CharField(max_length=200, blank=False, null= False, verbose_name="Direccion")
    comuna          = models.CharField(max_length=200, blank=False, null=False, verbose_name="Comuna")
    region          = models.CharField(max_length=50, blank=False, null=False, verbose_name="Region")
    descripcion     = models.TextField()
    img             = models.ImageField(upload_to='cards/')
    fecha           = models.DateField()
    cupos           = models.IntegerField()
    inscritos       = models.IntegerField(default=0)
    activo          = models.BooleanField(default=False)
    order           = models.IntegerField(default=0)

    class Meta:
        verbose_name    = 'Card'
        verbose_name_plural = 'Cards'
        ordering    = ['order']

    def _str_(self):
        return self.titulo

class CardsAdmin (SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields   = ['titulo']
    list_display    = ('titulo', 'order')
    list_per_page   = 10 # No of records per page


# PERFILES DE USUARIO (SOCIO, INVITADO, CAPITAN, ...)
class Perfil (models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    perfil          = models.CharField(max_length=30, blank=False, null=False, verbose_name= 'Perfil de usuario')
    descripcion     = models.TextField(blank=True, null=True, verbose_name='Descripcion del perfil')
    order           = models.IntegerField(default=0)

    class Meta: 
        verbose_name    = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering    = ['order']
    
    def __str__(self):
        return self.perfil

class PerfilesAdmin (SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields   = ['perfil']
    list_display    = ('perfil', 'order')
    list_per_page   = 10


# LA ESTRUCTURA DEL USUARIO QUE INTERACTUA CON EL SITIO CGM
class Usuario (models.Model):
    id                  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    rut                 = models.CharField(max_length=10, blank=False, null= False, verbose_name="Rut")
    primer_nombre       = models.CharField(max_length=200, blank=False, null=False, verbose_name= "Primer nombre")
    segundo_nombre      = models.CharField(max_length=200, blank=False, null=False, verbose_name= "Segundo nombre")
    apellido_paterno    = models.CharField(max_length=200, blank=False, null=False, verbose_name= "Apellido paterno")
    apellido_materno    = models.CharField(max_length=200, blank=False, null=False, verbose_name= "Apellido materno")
    fecha_nacimiento    = models.DateField(blank=False, null=False, verbose_name="Fecha de nacimiento")
    correo              = models.EmailField(max_length=200, blank=False, null=False, verbose_name="Correo electronico")
    telefono            = models.IntegerField(blank=False, null=False, verbose_name="Telefono movil")
    sexo                = models.CharField(max_length=1, choices= sexos, default= 'M')
    fecha_creacion      = models.DateField(auto_now_add=True, blank=True)
    # categoria         = a que categoria juega ej. Super Senior, Varones Senior,.. NOTA: averiguar si esto es un atributo del usuario o del torneo
    perfil              = models.ForeignKey(Perfil, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Perfil de usuario') #ej. socio, invitado, capitan, tesorero...
    estado              = models.CharField(max_length=1, choices= estado, default= 'A')  # en que estado se encuentra la cuenta ej. activa, inactiva, suspendida
    # socio_club        = si pertenece a un club, al parecer los de CGM tambien pertenecen a otros clubes ej. Prince of Wales Country Club, Club de Golf Las Araucarias, etc...  
    order               = models.IntegerField(default=0)

    class Meta:
        verbose_name    = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering    = ['order']

    def _str_(self):
        return self.rut
    
class UsuariosAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields   = ['rut']
    list_display    = ('rut', 'order')
    list_per_page   = 10


# LISTADO DE CLUBES DONDE SE REALIZAN LOS TORNEOS, TAL VEZ SE CELEBREN MÁS DE 1 TORNEO POR CLUB
class Club(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre          = models.CharField(max_length=50, blank=False, null=False, verbose_name='Nombre del club')
    abreviado       = models.CharField(max_length=10, blank=False, null=False, verbose_name='Nombre abreviado')
    direccion       = models.CharField(max_length=200, blank=False, null=False, verbose_name='Direccion')
    comuna          = models.CharField(max_length=50, blank=False, null=False, verbose_name='Comuna')
    ciudad          = models.CharField(max_length=50, blank=False, null=False, verbose_name='Ciudad')
    correo          = models.EmailField(max_length=200, blank=True, null=True, verbose_name='Correo electronico')
    telefono        = models.IntegerField(blank=True, null=True, verbose_name='Telefono')
    order           = models.IntegerField(default=0)

    class Meta:
        verbose_name    = 'Club'
        verbose_name_plural = 'Clubes'
        ordering    = ['order']

    def _str_(self):
        return self.nombre
    
class ClubesAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields   = ['nombre']
    list_display    = ('nombre', 'order')
    list_per_page   = 10


class Campeonato(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre          = models.CharField(max_length=50, blank=False, null=False, verbose_name='Nombre del campeonato')
    fecha           = models.DateField(verbose_name='Fecha de torneo')
    club            = models.ForeignKey(Club, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Club') # listado de clubes, deberia coincidir con el torneo
    bases           = models.FileField(upload_to='bases/') # bases del toreno, pdf
#    inscritos       = models.ForeignKey() # listado de inscritos actuales del torneo
#    salidas         = models.ForeignKey() # esquema de salida de los jugadores en el torneo
#    resultados      = models.ForeignKey() # listado posiciones del torneo segun distintos parametros
#    premiacion      = models.ForeignKey() # resumen de los primeros lugares por categoria
#    galeria         = models.ForeignKey() # galeria de fotos relacionados al torneo
    order           = models.IntegerField(default=0)
    
    class Meta:
        verbose_name    = 'Campeonato'
        verbose_name_plural = 'Campeonatos'
        ordering    = ['order']

    def _str_(self):
        return self.nombre
    

class CampeonatosAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields   = ['nombre']
    list_display    = ('nombre', 'order')
    list_per_page   = 10