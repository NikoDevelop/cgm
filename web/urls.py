from django.urls import path
from .views import *


urlpatterns = [
    path('' , home.as_view(), name = 'home'),
    path('historia' , historia.as_view(), name = 'historia'),
    path('noticia' , noticia.as_view(), name = 'noticia'),
    path('noticias', principal_noticias.as_view(), name = 'principal_noticias'),
    path('torneo', torneo.as_view(), name= 'torneo'),
]