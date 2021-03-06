from django.shortcuts import render
import requests
import json
from books.models import *
from django.contrib import messages


def list_books(request):
    req = requests.get('http://localhost:8000/books/?format=json')
    dicionario = json.loads(req.text)



    if request.POST:
        pesquisa = request.POST.get("pesquisa", None)
    
        req = None
        dicionario = None
        
        req = requests.get('http://localhost:8000/books/?title='+pesquisa)
        dicionario = json.loads(req.text)
        
        if not dicionario:
            req = requests.get('http://localhost:8000/books/?format=json')
            dicionario = json.loads(req.text) 

            messages.error(request,"Livro não encontrado!")

    print(dicionario)

    context = {
       "req" : dicionario
    }


    return render(request,"listar_livros.html",context)

def list_author(request):
    req = requests.get('http://localhost:8000/author/?format=json')
    dicionario = json.loads(req.text)
    
    
    listAutores = []
    for q in dicionario:
        livros =  requests.get('http://localhost:8000/books/?author='+str(q['id']))
        livros = json.loads(livros.text)
        obj = {
            'info':q,
            'livros':livros,
        }
        listAutores.append(obj)
    
    if request.POST:
        pesquisa = request.POST.get("pesquisa", None)

        req = requests.get('http://localhost:8000/author/?name='+pesquisa)
        dicionario = json.loads(req.text)

        if not dicionario:
            req = requests.get('http://localhost:8000/author/?format=json')
            dicionario = json.loads(req.text) 

            messages.error(request,"Autor não encontrado!")

    context = {
        "req" : listAutores,
        
    }


    return render(request,"listar_autor.html",context)


