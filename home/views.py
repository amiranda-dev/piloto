from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Teste Django')


def sobre(request):
    return HttpResponse('Sobre o sistema Django')