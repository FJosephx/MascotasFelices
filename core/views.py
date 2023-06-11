from django.shortcuts import render

# Create your views here.
def home(request):
    data = {'titulo': 'Mascotas Felices'}
    return render(request, 'core/index.html', data)

def ropa(request):
    data = {'titulo': 'Concurso de Ropa'}
    return render(request, 'core/ropa.html', data)

def ficha(request):
    data = {'titulo': 'Producto'}
    return render(request, 'core/ficha.html', data)

def registro(request):
    data = {'titulo': 'Registro'}
    return render(request, 'core/registro.html',data)

def login(request):
    data = {'titulo': 'Iniciar Sesion'}
    return render(request, 'core/login.html', data)

def administracion(request):
    data = {'titulo': 'Administracion'}
    return render(request, 'core/administracion.html',data)

def bodega(request):
    data = {'titulo': 'Bodega'}
    return render(request, 'core/bodega.html',data)

def boleta(request):
    data = {'titulo': 'Boleta'}
    return render(request, 'core/boleta.html',data)

def carrito(request):
    data = {'titulo': 'Carrito'}
    return render(request, 'core/carrito.html',data)

def miscompras(request):
    data = {'titulo': 'Mis Compras'}
    return render(request, 'core/miscompras.html',data)


def misdatos(request):
    data = {'titulo': 'Mis Datos'}
    return render(request, 'core/misdatos.html',data)

def nosotros(request):
    data = {'titulo': 'Nosotros'}
    return render(request, 'core/nosotros.html',data)

def usuarios(request):
    data = {'titulo': 'Admin. Usuarios'}
    return render(request, 'core/usuarios.html',data)

def productos(request):
    data = {'titulo': 'Admin. Productos'}
    return render(request, 'core/productos.html',data)

def ventas(request):
    data = {'titulo': 'Admin. Ventas'}
    return render(request, 'core/ventas.html',data)

