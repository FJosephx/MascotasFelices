from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def registro(request):
    return render(request, 'core/registro.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')