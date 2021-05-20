from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .matplot import comentariosGraficoCircular
from .matplot import comentariosGraficoBarras
from .forms import ContactoForm
from .forms import ComentarioForm


# Create your views here.

def home_page_view(request):
    return render(request, 'website/index.html')


def about_page_view(request):
    return render(request, 'website/about.html')


def benificios_page_view(request):
    return render(request, 'website/benificios.html')


def comentarios_page_view(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        context = {
            'form': form,
            'graphCir': comentariosGraficoCircular(),
            'graphBar': comentariosGraficoBarras()
        }
    else:
        context = {'form': form}

    return render(request, 'website/comentarios.html', context)


def estilos_page_view(request):
    return render(request, 'website/estilos.html')


def galeria_page_view(request):
    return render(request, 'website/galeria.html')


def provas_page_view(request):
    return render(request, 'website/provas.html')


def contacto_page_view(request):
    form = ContactoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:home'))

    context = {'form': form}

    return render(request, 'website/contacto.html', context)


def quizz_page_view(request):
    return render(request, 'website/quizz.html')
