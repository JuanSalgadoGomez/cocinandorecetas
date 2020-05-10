import datetime

from django.http import HttpResponse
from django.shortcuts import render


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def inicio(request):
    fechaActual = datetime.datetime.now()
    return render(request, "general/inicio.html", {"fecha_actual": fechaActual})


def saludo(request):  # primera vista
    p1 = Persona("Juan", "Salgado Gomez")
    equipo_trabajo = ["Maximiliano Persolja", "Alejandro Gonzalez", "Diego Perez", "Juan Salgado"]
    ahora = datetime.datetime.now()
    return render(request, "general/miplantilla.html",
                  {
                      "nombre_persona": p1.nombre,
                      "apellido_persona": p1.apellido,
                      "ahora": ahora,
                      "equipo": equipo_trabajo
                  })


def despedida(request):  # segunda vista
    return HttpResponse("PHP, que en paz descanse")


def obtenerFecha(request):
    fechaActual = datetime.datetime.now()
    documento = """
            <h1>
                Fecha y hora actuales %s
            </h1>""" % fechaActual
    return HttpResponse(documento)


def calcularEdad(request, edad, agno):
    # edadActual = 30
    periodo = agno - 2020
    edadFutura = edad + periodo
    documento = "<h1>En el año %s tendras %s años" % (agno, edadFutura)
    return HttpResponse(documento)
