from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .matplot import comentariosGraficoCircular, comentariosGraficoBarras, quizzPessoal, quizzGrupo
from .forms import ContactoForm, ComentarioForm, QuizzForm

# Create your views here.
from .models import Contacto


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


def contactoLista_page_view(request):
    context = {'contactos': sorted(Contacto.objects.all(), key=lambda objeto: objeto.id)}
    return render(request, 'website/contactoLista.html', context)


def contactoEditar_page_view(request, contacto_id):
    contacto = Contacto.objects.get(pk=contacto_id)
    form = ContactoForm(request.POST or None, instance=contacto)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:home'))

    context = {'form': form, 'contacto_id': contacto_id}
    return render(request, 'website/contactoEditar.html', context)


def contactoApaga_page_view(request, contacto_id):
    Contacto.objects.get(pk=contacto_id).delete()
    return HttpResponseRedirect(reverse('website:home'))


def quizz_page_view(request):
    form = QuizzForm(request.POST or None)
    if form.is_valid():
        quizz = form.save()
        return HttpResponseRedirect(reverse('website:quizzResult', args=(quizz.id,)))

    context = {
        'form': form,
    }
    return render(request, 'website/quizz.html', context)


def quizzResult_page_view(request, id):
    context = {
        'graphPessoal': quizzPessoal(id),
        'graphGrupo': quizzGrupo(id),
    }
    return render(request, 'website/quizzResult.html', context)
