from django.shortcuts import render
import requests
from django.http import JsonResponse

def home(request):
    return render(request, 'meuapp/home.html')

def consultar_cep(request):
    
   
    cep = '58036555'
    
    url= f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url)

    dados = resposta.json()

    return JsonResponse(dados)
