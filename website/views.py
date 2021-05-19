from django.shortcuts import render


# Create your views here.

def home_page_view(request):
    return render(request, 'website/index.html')


def about_page_view(request):
    return render(request, 'website/about.html')


def benificios_page_view(request):
    return render(request, 'website/benificios.html')


def comentarios_page_view(request):
    return render(request, 'website/comentarios.html')


def estilos_page_view(request):
    return render(request, 'website/estilos.html')


def galeria_page_view(request):
    return render(request, 'website/galeria.html')


def provas_page_view(request):
    return render(request, 'website/provas.html')


def contacto_page_view(request):
    return render(request, 'website/contacto.html')


def quizz_page_view(request):
    return render(request, 'website/quizz.html')
