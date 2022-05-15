from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'servicios/presentacion.html')


def acerca(request):
    return render(request, 'servicios/acerca.html')

def profesionales(request):
    return render(request, 'servicios/profesionalesTeam.html')

def detalleMedico(request):
    return render(request, 'servicios/detalleMedico.html')

def receta(request):
    return render(request, 'servicios/receta.html')

def ubicacion(request):
    return render(request, 'servicios/ubicacion.html')

def galeria(request):
    return render(request, 'servicios/galeria.html')


def testimonio(request):
    return render(request, 'servicios/testimonio.html')
    