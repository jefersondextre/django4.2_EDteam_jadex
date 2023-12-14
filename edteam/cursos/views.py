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


def holamundo(request):
    print(request.headers)
    return HttpResponse('<h1>Hola mundo con Django 4.2</h1>',
                        header={"Content-Type": "application/pdf",
                                "Content-Disposition": "attachment; filename='foo.pdf'"
                                }     
    )
#                       header={"Content-Type": "application/vnd.ms-excel",
#                               "Content-Disposition": "attachment; filename='foo.xls'"
#                               } 
# 

def saludo(request):
    nombre = request.GET['nombre']
    return HttpResponse("<center>" + nombre + "</center>")


def suma(request, n1 ,n2):
    resultado = n1 + n2
    return HttpResponse("El resultado es "+  str(resultado))