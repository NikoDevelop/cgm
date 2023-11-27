import uuid
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from search_admin_autocomplete.admin import SearchAutoCompleteAdmin
from .choices import sexos, estado

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
    
class UsuarioManager(BaseUserManager):
    def _create_user(self,username,email,primer_nombre,apellido_paterno,password,is_staff,is_superuser, **extra_fields):
        user = self.model(
            username= username, 
            email= self.normalize_email(email),                
			primer_nombre= primer_nombre,       
			apellido_paterno= apellido_paterno,
            is_staff = is_staff,  
            is_superuser = is_superuser,  
            **extra_fields
        )
        
        user.set_password(password)
        user.save(using=self.db)
        return user

    
    def create_user(self, username,email,primer_nombre,apellido_paterno,password = None, is_staff = True , is_superuser=False,**extra_fields):
        return self._create_user(username,email,primer_nombre,apellido_paterno,password , is_staff = is_staff, is_superuser= is_superuser, **extra_fields)
    

    def create_superuser(self, username,email,primer_nombre,apellido_paterno,password = None, is_staff = True , is_superuser=True,**extra_fields):
        return self._create_user(username,email,primer_nombre,apellido_paterno,password , is_staff = is_staff, is_superuser= is_superuser, **extra_fields)
    

class Usuario (AbstractBaseUser, PermissionsMixin):
    id                  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    username            = models.CharField(max_length=10, blank=False, null= False,unique = True, verbose_name="Rut")
    email               = models.EmailField('Correo Electrónico', max_length=254,unique = True)
    primer_nombre       = models.CharField(max_length=200, blank=False, null=False, verbose_name= "Primer nombre")
    segundo_nombre      = models.CharField(max_length=200, blank=True, null=False,  verbose_name= "Segundo nombre")
    apellido_paterno    = models.CharField(max_length=200, blank=False, null=False, verbose_name= "Apellido paterno")
    apellido_materno    = models.CharField(max_length=200, blank=True, null=False, verbose_name= "Apellido materno")
    fecha_nacimiento    = models.DateField(blank=True, null=True, verbose_name="Fecha de nacimiento")
    telefono            = models.IntegerField(blank=True, null=True, verbose_name="Telefono movil")

    perfil              = models.ForeignKey(Perfil, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Perfil de usuario') #ej. socio, invitado, capitan, tesorero...
    estado              = models.CharField(max_length=1, choices= estado, default= 'A', null=True)  # en que estado se encuentra la cuenta ej. activa, inactiva, suspendida
    
    is_staff        = models.BooleanField('Staff',default = False)  # requerido para ingresar al admin default
    is_superuser    = models.BooleanField('Administrador',default = False)# requerido para ingresar al admin default
    objects         = UsuarioManager()

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['primer_nombre','apellido_paterno','email']

    class Meta:
        verbose_name    = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering    = ['apellido_paterno']

    def __str__(self):
        return self.username
    
class UsuariosAdmin(SearchAutoCompleteAdmin, admin.ModelAdmin):
    search_fields   = ['username','apellido_paterno']
    list_display    = ('apellido_paterno', 'primer_nombre','username','password')
    list_per_page   = 10