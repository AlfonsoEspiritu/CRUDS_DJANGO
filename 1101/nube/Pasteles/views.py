from django.shortcuts import render
from .models import pastel
from .forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms 
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin 
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def listar(request):
    pasteles= pastel.objects.all()
    template="listarPa.html"
    context={
        'Pasteles': pasteles,

    }
    return render (request,template,context)

def crear(request): 
    if request.method=='POST':
        form=pastel2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarPastel')

    form = pastel2 
    context={
        'form':form,

    }
    return render (request, "agregarPa.html", context)
def eliminar(request, id):
  member = pastel.objects.get(id=id)
  member.delete()
  return redirect(reverse('listarPastel'))

def actualizar(request, id):
    if request.method=='POST':
        instance=pastel.objects.get(id=id)
        form=pastel2(request.POST or None, instance=instance)
        print('\n\n\n\n\n\n\n\n IN \n\n\n\n\n\n\n\n')
        if form.is_valid():
            form.save()
            print('\n\n\n\n\n\n\n\n OUT \n\n\n\n\n\n\n\n')

            return redirect('listarPastel')
        else: 
            template = 'actualizarPa.html'
            dato = pastel.objects.get(id=id)
            context = {
                'errors': form.errors,
                'dato': dato,
                #'form':form,
            }
            return render(request, template, context)

    
    dato = pastel.objects.get(id=id)
    #form= agregar()
    #form=mymember
    template = 'actualizarPa.html'
    context = {
    'dato': dato,
    #'form':form,
    }
    return render(request, template, context)

# Create your views here.
