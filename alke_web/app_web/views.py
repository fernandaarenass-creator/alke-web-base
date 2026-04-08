from django.shortcuts import render

def inicio(request):
    
    datos = {
        'nombre_proyecto': 'Alke Web Base',
        'modulo': 'Módulo 6: Desarrollo Web con Django',
        'empresa': 'Alke Solutions'
    }
    return render(request, 'inicio.html', datos)