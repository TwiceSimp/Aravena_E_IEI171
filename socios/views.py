from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import FormSocios
from .models import Socios

# Create your views here.

def index(request):
    return render(request, 'socios/index.html')

def listadoSocios(request):
    socio = Socios.objects.all()
    data = {'soci' : socio}
    return render (request,'socios/socios.html',data)

def agregarSocio(request):
    form = FormSocios()
    if (request.method == 'POST'):
        form = FormSocios(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('listadoSocios')

    data = {'form' : form}
    return render (request, 'socios/formulario.html',data)


def eliminarSocio(request,id):
    soc = Socios.objects.get(id = id)
    soc.delete()
    return redirect ('/socios')


def editarSocios(request, id):
    pro = Socios.objects.get(id = id)
    form = FormSocios(instance=pro)

    if (request.method == 'POST'):
        form = FormSocios(request.POST, instance=pro)
        if (form.is_valid()):
            form.save()
        return listadoSocios(request)

    data = {'form': form}
    return render(request, 'socios/actualizar.html',data)
    


