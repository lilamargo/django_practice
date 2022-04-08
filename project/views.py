from django.template import Template, Context
from django.http import HttpResponse
import datetime
from django.shortcuts import render

# Request: Para realizar peticiones.
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP.

def home(request):  # Aqui pasamos un objeto de tipo request como primer argumento.
    return HttpResponse("<p style='color: blue'>Home</p>")

def bienvenida(request):  # Aqui pasamos un objeto de tipo request como primer argumento.
    return HttpResponse("<p style='color: blue'>Bienvenido a este sitio</p>")

def categoriaEdad(request, edad): 
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera Edad"
        else:
            categoria = "Adultez"
    else:
        if edad < 10:
            categoria = "infancia"
        else:
            categoria = "adolescencia"
    
    resultado = "<h1>Categoria de la edad: %s</h1>" %categoria
    return HttpResponse(resultado)


def obtenerMomentoActual(request):
    # respuesta = "<h1>Momento Actual: {0}</h1>".format(datetime.datetime.now()) # Con formato por default
    respuesta = "<h1>Momento Actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S")) # Con formato simple
    return HttpResponse(respuesta)

def contenidoHTML(request, nombre, edad):
    contenido = """
    <html>
    <body>
    <p>Edad: %s / Edad: %s</p>
    </body>  
    </html>
    """ % (nombre, edad)
    return HttpResponse(contenido)

def plantillaExterna1(request):
    # Abrimos el documento que contiene a la plantilla
    plantillaExterna = open('D:/PROYECTOS LAP/S2G Energy/Django_Proyecto/project/plantillas/plantilla1.html')
    # Cargar el documento en una variable de tipo Template
    template = Template(plantillaExterna.read())
    #Cerrar el documento externo que hemos abierto
    plantillaExterna.close()
    # Objeto que nos permite indicar que atributos va a utilizar la plantilla... 
    # ...contenedor para poder pasarle parámetros y sean procesados por la plantilla
    contexto = Context() 
    # Renderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento)



