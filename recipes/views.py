# Ler arquivos e renderizá-los (HTML/CSS)
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request):
    return render(request, 'home.html')


def contact_view(request):
    return HttpResponse("AQUI ESTÁ A PÁGINA DE CONTATO de RECEITAS")


def about_view(request):
    return HttpResponse("AQUI ESTÁ A PÁGINA SOBRE O AUTOR DE RECEITAS")
