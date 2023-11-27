from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('' , home.as_view(), name = 'home'),
    path('historia' , historia.as_view(), name = 'historia'),
    path('noticia/<slug:slug>/' , noticia.as_view(), name = 'noticia'),
    path('noticias', principal_noticias.as_view(), name = 'noticias'),
    path('torneos', torneos.as_view(), name= 'torneos'),

    path('ranking', ranking.as_view(), name= 'ranking'),
    path('404', notFound404.as_view(), name= '404'),

    path('comite', comite.as_view(), name="comite"),
    path('directorio', directorio.as_view(), name='directorio'),

]