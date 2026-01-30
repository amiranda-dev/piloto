from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Teste Django')


def sobre(request):
    return HttpResponse('Sobre o sistema Django')


def contato(request):
    return HttpResponse('Esta é uma página de contato')


def ajuda(request):
    return HttpResponse('Está é a página de ajuda.')