from django.contrib import admin
from django.urls import path
from .views import*
import re
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from .views import *



urlpatterns = [
    path('listarPi/',listar,name="listar"),
    path('agregarPi/', crear, name='agregar'),
    path('eliminarPi/<int:id>',eliminar,name='eliminar'),
    path('actualizarPi/<int:id>',actualizar,name='actualizar'),
]