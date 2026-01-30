from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')


def ajuda(request):
    return render(request, 'ajuda.html')


def item(request, id):
    return render(request, 'exibir_item.html', {'id':id})


def perfil(request, usuario):
    return render(request, 'perfil.html', {'usuario':usuario})


def dia_semana(request, dia):
    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    nome_dia = dias.get(dia, "Dia inválido")
    
    return render(request, 'diasemana.html', {'nome_dia': nome_dia})