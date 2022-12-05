from django.shortcuts import render
from .models import pizza
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
    pizzeria= pizza.objects.all()
    template="listarPi.html"
    context={
        'Pizzeria': pizzeria,

    }
    return render (request,template,context)

def crear(request): 
    if request.method=='POST':
        form=pizza2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')

    form = pizza2 
    context={
        'form':form,

    }
    return render (request, "agregarPi.html", context)
def eliminar(request, id):
  member = pizza.objects.get(id=id)
  member.delete()
  return redirect(reverse('listar'))

def actualizar(request, id):
    if request.method=='POST':
        instance=pizza.objects.get(id=id)
        form=pizza2(request.POST or None, instance=instance)
        print('\n\n\n\n\n\n\n\n IN \n\n\n\n\n\n\n\n')
        if form.is_valid():
            form.save()
            print('\n\n\n\n\n\n\n\n OUT \n\n\n\n\n\n\n\n')

            return redirect('listar')
        else: 
            template = 'actualizarPi.html'
            dato = pizza.objects.get(id=id)
            context = {
                'errors': form.errors,
                'dato': dato,
                #'form':form,
            }
            return render(request, template, context)

    
    dato = pizza.objects.get(id=id)
    #form= agregar()
    #form=mymember
    template = 'actualizarPi.html'
    context = {
    'dato': dato,
    #'form':form,
    }
    return render(request, template, context)


# Create your views here.