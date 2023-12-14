from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def cursos(request):
    return HttpResponse('<center> <h1>Mi curso EDteam </h1></center>')