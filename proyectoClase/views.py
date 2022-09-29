from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random

from home.models import Persona, Familiar

def hola(request):
    return HttpResponse('<h1>Buenas clase 41765!</h1>')

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_y_hora}')

def calcular_fecha_nac(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años sería {fecha}')

def mi_template(request):
    cargar_archivo = open(r'D:\Trabajo_con_python\Proyectos_Curso\proyecto_clases\templates\mi_template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def tu_template(request, nombre):
 
    template = loader.get_template('tu_template.html')
    template_renderizado = template.render({'persona': nombre})
    return HttpResponse(template_renderizado)

def prueba_template(request):
    mi_contexto = {'rango':list(range(1,11)),
                   'valor_aleatorio': random.randrange(1,11)
                   }
    template = loader.get_template('prueba_template.html')
    template_renderizado = template.render(mi_contexto)
    return HttpResponse(template_renderizado)

def crear_persona(request, nombre, apellido):
    persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1,99),fecha_nacimiento=datetime.now())
    persona.save()
    
    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render({'persona':persona})
    return HttpResponse(template_renderizado)

def ver_personas(request):
    
    personas = Persona.objects.all()
    
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas':personas})
    
    return HttpResponse(template_renderizado)

def crear_familiar(request):    
    persona1 = Familiar(nombre='Ricardo', parentezco='Padre', edad=78,fecha_nacimiento = datetime(1934,7,11))
    persona2 = Familiar(nombre='Gerardo', parentezco='Pareja', edad=62,fecha_nacimiento = datetime(1960,1,1))
    persona3 = Familiar(nombre='Mauro', parentezco='Hijo', edad=27,fecha_nacimiento = datetime(1995,7,29))
    persona1.save()
    persona2.save()
    persona3.save()
    template = loader.get_template('crear_familiar.html')
    template_renderizado = template.render({})
    return HttpResponse(template_renderizado)

def ver_familiares(request):
    
    familiares = Familiar.objects.all()
    
    template = loader.get_template('ver_familiares.html')
    template_renderizado = template.render({'familiares':familiares})
    
    return HttpResponse(template_renderizado)