# PAGINA ONDE FAZ OS GRAFICOS MATPLOTLIB
from io import StringIO

from matplotlib import pyplot as plt

from .models import Comentario


def comentariosGraficoCircular():
    comentarios = Comentario.objects.all()
    listaKeys = ['Rigor', 'Clareza', 'Precisao']
    rigor = 0
    clareza = 0
    precisao = 0
    listaValues = []
    for coment in comentarios:
        rigor += int(coment.rigor)
        clareza += int(coment.clareza)
        precisao += int(coment.precisao)
    listaValues.append(rigor)
    listaValues.append(clareza)
    listaValues.append(precisao)

    fig = plt.figure()
    plt.pie(listaValues, labels=listaKeys, autopct='%1.0f%%')
    plt.title("Gráfico Critérios de Avaliação")
    fig.set_facecolor((0.921, 0.921, 0.921))
    fig.set_size_inches(4, 2.666)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data


def comentariosGraficoBarras():
    comentarios = Comentario.objects.all()
    listaKeys = ['F. Ler', 'Boa Opti', 'T. Resposta', 'F. Usar']
    ler = 0
    opt = 0
    tem = 0
    usar = 0
    listaValues = []
    for coment in comentarios:
        if coment.facilLer:
            ler += 1
        if coment.optimizacao:
            opt += 1
        if coment.tempoResposta:
            tem += 1
        if coment.facilUsar:
            usar += 1
    listaValues.append(ler)
    listaValues.append(opt)
    listaValues.append(tem)
    listaValues.append(usar)

    fig = plt.figure()
    plt.bar(listaKeys, listaValues)
    plt.title("Gráfico Critérios Considerados")
    fig.set_facecolor((0.921, 0.921, 0.921))
    fig.set_size_inches(4, 2.666)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    return data
