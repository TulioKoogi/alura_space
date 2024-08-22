from django.shortcuts import render
from django.http import HttpResponse

def index(args):
    return HttpResponse('<h1>Alura Space</h1><p>Seja bem vindo ao Espaço</p>')
