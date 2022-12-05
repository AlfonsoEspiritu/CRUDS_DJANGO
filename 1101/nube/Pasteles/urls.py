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
    path('listarPa/',listar,name="listarPastel"),
    path('agregarPa/', crear, name='agregarPastel'),
    path('eliminarPa/<int:id>',eliminar,name='eliminarPastel'),
    path('actualizarPa/<int:id>',actualizar,name='actualizarPastel'),
]