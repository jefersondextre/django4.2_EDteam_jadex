from django.shortcuts import render

from django.http import HttpResponse

from .models import TblCurso
# Create your views here.

def cursos(request):
        listaCursos = TblCurso.objects.all()
        print(listaCursos)
        strCursos = "<ul>"
        for curso in listaCursos:
            strCursos += "<li>"+curso.curso_titulo+"</li>"
            
        strCursos += "</ul>"
        return HttpResponse('<center> <h1>Mi curso EDteam </h1></center>')