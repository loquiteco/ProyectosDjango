from django.http import HttpResponse
import datetime
from django.template import Template, Context

# creacion de nuestra primera vista

def saludo(request):

    return HttpResponse("HOLA DEVELOPER")

def despedida(request):

    doc_externo=open("C:/Users/andres.suescun/OneDrive - AGUAS DE BOGOTA S.A ESP/ANDRES FELIPE SUESCUN ANGARITA/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context()

    documento=plt.render(ctx)

    return HttpResponse(documento)


    # EJERCICIOS ACD. CONTENIDO DINAMICO

def dameFecha(request):
    fechaActual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h2>Fecha y hora actuales %s </h2>
    </body>
    </html>""" % fechaActual

    return HttpResponse(documento) 

    # EJERCICIOS CON URLS

def calculaEdad(request, edad, anno):

    periodo=anno-2022
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendrás %s años" %(anno, edadFutura)
    
    return HttpResponse(documento)


