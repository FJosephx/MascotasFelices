from django.shortcuts import render, redirect
from .models import Producto, CategoriaProducto
from .forms import ProductoForm
# Create your views here.
def home(request):
    data = {'titulo': 'Mascotas Felices', 
            "list": Producto.objects.all().order_by('idProducto'),}
    return render(request, 'core/index.html', data)

def ropa(request):
    data = {'titulo': 'Concurso de Ropa'}
    return render(request, 'core/ropa.html', data)

def ficha(request, id):
    producto = Producto.objects.get(idProducto=id)
    data = {'titulo': 'Producto', "producto": producto}
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


def ventas(request):
    data = {'titulo': 'Admin. Ventas'}
    return render(request, 'core/ventas.html',data)



def productos(request, action, id):
    
    data = {'titulo': 'Admin. Productos', 
            "mesg": "", 
            "form": ProductoForm, 
            "action": action, 
            "id": id}
    
    if action == 'ins':
        if request.method == "POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El Producto fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se pueden crear dos productos con el mismo id!"

    elif action == 'upd':
        objeto = Producto.objects.get(idProducto=id)
        if request.method == "POST":
            form = ProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El Producto fue actualizado correctamente!"

        data["form"] = ProductoForm(instance=objeto)
        data["imagenProducto_url"] = objeto.imagenProducto.url


    elif action == 'del':
        try:
            Producto.objects.get(idProducto=id).delete()
            data["mesg"] = "¡El Producto fue eliminado correctamente!"
            return redirect(Producto, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El Producto ya estaba eliminado!"

    
    data["list"] = Producto.objects.all().order_by('idProducto')


    return render(request, 'core/productos.html',data)
