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
        listado = Listado.objects.filter(tipo="7913628f-ab4f-4016-ac4e-bce8261fa801")
        # print('aca')
        # print(front)
        #personal = Personal.objects.order_by('order')

        # contexto['front']  = list(front.values('titulo','img', 'contenido', 'order'))[0]
        contexto['front']  = list(front.values('titulo','img', 'contenido', 'order'))
        contexto['listado'] = list(listado.values('titulo', 'img', 'order'))
        # print(contexto['front'] )
        #contexto['personal']  = list(front.values('titulo','img', 'tipo', 'subtitulo', 'order'))

        print("hola", front.values('titulo')) 
        return contexto

# Create your views here.
class noticia(TemplateView):
    template_name = "views/noticia.html"
    # template_name = "root/empty.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nameWeb"] = nameWeb
        contexto["title"] = "noticia"
        front = Front.objects.filter(titulo="noticia")
        listado = Listado.objects.filter(tipo="9dda77c3-bcb3-46f8-bfec-4450dc518688")
        # print('aca')
        # print(front)
        #personal = Personal.objects.order_by('order')

        # contexto['front']  = list(front.values('titulo','img', 'contenido', 'order'))[0]
        contexto['front']  = list(front.values('titulo','img', 'contenido', 'order'))
        contexto['listado'] = list(listado.values('titulo', 'img', 'order'))
        # print(contexto['front'] )
        #contexto['personal']  = list(front.values('titulo','img', 'tipo', 'subtitulo', 'order'))

        print("hola", front.values('titulo')) 
        return contexto

# Create your views here.
class principal_noticias(TemplateView):
    template_name = "views/principal_noticias.html"
    # template_name = "root/empty.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nameWeb"] = nameWeb
        contexto["title"] = "noticia"
        front = Front.objects.filter(titulo="noticia")
        listado = Listado.objects.filter(tipo="9dda77c3-bcb3-46f8-bfec-4450dc518688")
       
        contexto['front']  = list(front.values('titulo','img', 'contenido', 'order'))
        contexto['listado'] = list(listado.values('titulo', 'img', 'order'))
      
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