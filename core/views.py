from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello Word, {nome.title()}, {idade} anos</h1>')


def soma(request, num1, num2):
    return HttpResponse(num1+num2)


def subtracao(request, num1, num2):
    return HttpResponse(num1 - num2)


def multiplicacao(request, num1, num2):
    return HttpResponse(num1 * num2)


def divisao(request, num1, num2):
    return HttpResponse(num1 / num2)