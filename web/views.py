# from django.shortcuts import render

# Create your views here.

from typing import Any
from django.shortcuts import render
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    UpdateView,
    CreateView,
    DeleteView,
    DetailView,
)
from .models import *
from django.core.paginator import Paginator

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy

from django.shortcuts import render,redirect

from .forms import *
from .mixins import *


nameWeb = "CGM"


# Create your views here.
class home(TemplateView):
    template_name = "views/home.html"
    # template_name = "root/empty.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nameWeb"] = nameWeb
        contexto["title"] = "home"

        galeria = Galeria.objects.order_by('order')
        link = Links.objects.order_by('order')
        # front = Front.objects.filter(titulo="historia")
        
        # print(galeria)

        if len(galeria)==0:
            print('hola')

        contexto['galeria']  = list(galeria.values('titulo','img', 'order'))
        contexto['link']  = list(link.values('titulo','img', 'parrafo', 'order'))
        # contexto['front']  = list(front.values('titulo','img', 'contenido', 'order'))
        # #contexto['personal']  = list(front.values('titulo','img', 'tipo', 'subtitulo', 'order'))

        return contexto


# Create your views here.
class historia(TemplateView):
    template_name = "views/historia.html"
    # template_name = "root/empty.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nameWeb"] = nameWeb
        contexto["title"] = "historia"
        front = Front.objects.filter(titulo="historia")
        
        #listado = Listado.objects.filter(tipo='presidentes')
        listado = Listado.objects.filter(tipo="7913628f-ab4f-4016-ac4e-bce8261fa801")

        # contexto['front']  = list(front.values('titulo','img', 'contenido', 'order'))[0]
        contexto['front']  = list(front.values('titulo','img', 'contenido', 'order'))
        contexto['listado'] = list(listado.values('titulo', 'img', 'order'))
        # print(contexto['front'] )
        #contexto['personal']  = list(front.values('titulo','img', 'tipo', 'subtitulo', 'order'))

        return contexto

# Create your views here.
class noticia(DetailView):
    model = Noticia
    template_name = "views/noticia.html"
   
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nameWeb"] = nameWeb
        contexto["title"] = "noticia"
        dato =  self.get_object()
        contexto['new'] =  dato
        lista = []
        if(dato['img1']!=''):
            lista.append(dato['img1'])
        if(dato['img2']!=''):
            lista.append(dato['img2'])
        if(dato['img3']!=''):
            lista.append(dato['img3'])
        if(dato['img4']!=''):
            lista.append(dato['img4'])
        if(dato['img5']!=''):
            lista.append(dato['img5'])

        contexto['imgs']= lista
        contexto['front']= [{'img': dato['img']}]

        return contexto

    def get_object(self, **kwargs):
        print('slug', self.kwargs.get('slug', None))
        slug =  self.model.objects.filter(slug = self.kwargs.get('slug', None))
        print('slug1', slug )
        slug = list(slug.values('titulo','img','fecha','resumen','info','slug','img1', 'img2', 'img3','img4','img5','lugar'))
        print('slug2', slug)
        return slug[0]

# Create your views here.
class principal_noticias(TemplateView):
    model = Noticia
    template_name = "views/principal_noticias.html"
    
    def get_queryset(self):
        
        lNoticia = self.model.objects.filter(is_active=True).filter(is_aprobado=True).order_by('fecha')
        lNoticia = list(lNoticia.values('titulo', 'img', 'fecha','resumen','lugar'))
        paginator = Paginator(lNoticia,3)
        page = self.request.GET.get('page')
        lNoticia = paginator.get_page(page)
            
        return lNoticia


    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nameWeb"] = nameWeb
        contexto["title"] = "noticias"
        contexto['datos'] = self.get_queryset()

        if contexto['datos'].paginator.num_pages > 1 and contexto['datos'].number != contexto['datos'].paginator.num_pages : # tiene un next
            if contexto['datos'].paginator.num_pages - contexto['datos'].next_page_number() > 1:
                contexto['up'] = True     
            else:
                contexto['up'] = False 
        if contexto['datos'].paginator.num_pages > 2 and contexto['datos'].number != 1 : # hay un previo
            if contexto['datos'].previous_page_number()  - 1 > 1:
                contexto['down'] = True     
            else:
                contexto['down'] = False 

        return contexto

class torneo(TemplateView):
    template_name = "views/torneo.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nameWeb"] = nameWeb
        contexto["title"] = "torneo"
        mainCard = Card.objects.filter(activo = True)
        torneoCard = Card.objects.filter(activo = False)
        contexto['mainCard'] = list(mainCard.values('titulo', 'direccion', 'comuna', 'region', 'descripcion', 'img', 'fecha', 'cupos', 'inscritos', 'order'))
        contexto['torneoCard'] = list(torneoCard.values('titulo', 'direccion', 'comuna', 'region', 'descripcion', 'img', 'fecha', 'cupos', 'inscritos', 'order'))
        contexto['gato'] = list(mainCard.values('titulo'))[0]
        #print(contexto['mainCard'][0].titulo)
        return contexto



class ranking(TemplateView):
    template_name = "views/ranking.html"
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nameWeb"] = nameWeb

        contexto["title"] = "ranking"
        front = Front.objects.filter(titulo="ranking")
        contexto['front']  = list(front.values('titulo','img', 'contenido', 'order','file'))
        
        return contexto

class notFound404(TemplateView):
    template_name = "views/404.html"

    def get_context_data(self,**kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['nameWeb'] = nameWeb
        contexto['title'] = '404'
        front = Front.objects.filter(titulo="404")
        datos = list(front.values('titulo','img', 'contenido'))
        if len(datos ) > 0:
            contexto['front'] =  datos
            contexto['h1']     = datos[0]['contenido']
        else:
            contexto['front'] = []
            contexto['h1']     = 'No hay sitio'
        print('contexto') 
        print(contexto['front'])

        return contexto  
class Login(FormView):
    
    template_name = 'views/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('home')
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self,request,*args,**kwargs):
        return super(Login,self).dispatch(request,*args,**kwargs)
    
    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        contexto = super(Login, self).get_context_data(**kwargs)
        contexto['nameWeb'] = nameWeb
        contexto['title'] = 'ACCESO AL CLUB' 
        contexto['loginClass'] = 'loginClass'

        contexto['error'] = False

        return self.render_to_response(contexto)

    def form_invalid(self, form, **kwargs):
        contexto =  super(Login, self).get_context_data(**kwargs)
        contexto['nameWeb'] = nameWeb
        contexto['title'] = 'LOGIN'
        contexto['loginClass'] = 'loginClass'
        contexto['error'] = True
        return self.render_to_response(contexto)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')


class comite(TemplateView):
    template_name = "views/comite.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nameWeb"] = nameWeb
        contexto["title"] = "comite"
        
        front = Front.objects.filter(titulo="comite")
        #listado_rc = Listado.objects.filter(tipo__tipo="ComisionRC")
        listado = Listado.objects.filter(tipo__tipo__in=['ComisionRC','ComisionED', 'Responsable Institucional'])

        contexto['front']  = list(front.values('titulo','img', 'contenido', 'order'))
        contexto['listado'] = list(listado.values('titulo', 'img', 'tipo__tipo', 'order'))

        return contexto


# Create your views here.
class directorio(TemplateView):
    template_name = "views/directorio.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nameWeb"] = nameWeb
        contexto["title"] = "directorio"
        front = Front.objects.filter(titulo="directorio")
        listado_m = Listado.objects.filter(tipo__tipo__in=['Directorio'])
        listado_c = Listado.objects.filter(tipo__tipo__in=['Capitan'])
        listado_p = Listado.objects.filter(tipo__tipo__in=['Presidentes'])

        contexto['front']  = list(front.values('titulo','img', 'contenido', 'order'))
        contexto['listado_m'] = list(listado_m.values('titulo', 'img', 'order', 'tipo__tipo', 'order'))
        contexto['listado_c'] = list(listado_c.values('titulo', 'img', 'order', 'tipo__tipo', 'order'))
        contexto['listado_p'] = list(listado_p.values('titulo', 'img', 'order', 'tipo__tipo', 'order'))
        
        return contexto

