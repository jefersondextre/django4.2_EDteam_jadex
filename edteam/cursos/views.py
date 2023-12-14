from django.shortcuts import render
# -------------------
from django.http import HttpResponse
from django.http import JsonResponse

from .models import TblCurso

# Create your views here.
def cursos(request):
        listaCursos = TblCurso.objects.all()
        print(listaCursos)
        strCursos = "<ul>\n"
        for curso in listaCursos:
            strCursos += "<li>"+curso.curso_titulo+"</li>"
        strCursos += "</ul>"
        
        return HttpResponse("<center> <h1>Mi curso EDteam </h1></center>"+strCursos)
    
    
def cursosApi(request):
    listaCursos = TblCurso.objects.all()
    listaFinal=[]
    for curso in listaCursos:
        dictCurso = {
            'id':curso.curso_id,
            'titulo':curso.curso_titulo,
            'descripcion':curso.curso_descripcion
        }
        listaFinal.append(dictCurso)
        
    dataJson = {
        'data': listaFinal
    }
        
    return JsonResponse(dataJson)