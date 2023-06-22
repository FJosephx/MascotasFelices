from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
import locale
# Create your views here.

# def home(request):
#     data = {'titulo': 'Mascotas Felices', 
#             "list": Producto.objects.all().order_by('id'),}
#     return render(request, 'core/index.html', data)


# def home(request):
#     data = {'titulo': 'Mascotas Felices', 
#             "list": Producto.objects.all().order_by('id'),}
#     return render(request, 'core/index.html', data)

def home(request):
     resultado=''
     
     list = Producto.objects.all().order_by('nombre')
     if request.method == 'POST':
         buscar = request.POST.get('buscar')
         if buscar.strip() != '':
             resultado = buscar
             list = Producto.objects.filter(nombre__icontains=buscar).order_by('nombre')
             
     data = { 
         'titulo': 'Mascotas Felices', 
         'list': list,
         'resultado': resultado
     }
     return render(request, 'core/index.html', data)


# def index(request):
    # conseguir productos
    # productos = Producto.objects.all()
    # otra forma de traer los productos a la lista
    # data = { 'productos': Producto.objects.all() }

    # cambiar porcentaje a TODOS los productos
    # recorre cada producto de la lista
    # for producto in productos:
    #     producto.descuento_subscriptor = 6
    #     producto.save()
    
    # contar los productos
    # Producto.objects.count()
    
    # se tienen que retornar los productos a travez de un JSON
    # data = { 'productos': productos }
        
    # return render(request, 'core/index.html', data)


def ropa(request):
    data = {'titulo': 'Concurso de Ropa'}
    return render(request, 'core/ropa.html', data)

def ficha(request, id):
    producto = Producto.objects.get(id=id)


    data = {'titulo': producto.nombre, 
            "producto": producto, 
            "nombre": producto.nombre,

            }
    
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
                    data["mesg_class"] = "ins"
                except:
                    data["mesg"] = "¡No se pueden crear dos productos con el mismo id!"
                    data["mesg_class"] = "ins"
    elif action == 'upd':
        objeto = Producto.objects.get(id=id)
        if request.method == "POST":
            form = ProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El Producto fue actualizado correctamente!"
                data["mesg_class"] = "success"

        data["form"] = ProductoForm(instance=objeto)
        data["imagen_url"] = objeto.imagen.url


    elif action == 'del':
        try:
            Producto.objects.get(id=id).delete()
            data["mesg"] = "¡El Producto fue eliminado correctamente!"
            data["mesg_class"] = "error"

            return redirect(Producto, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El Producto ya estaba eliminado!"
            data["mesg_class"] = "error"
    

    data["list"] = Producto.objects.all().order_by('id')

    
    # productos = Producto.objects.all()
    # para usar el for y cambiar a todas las tablas
    # hay que crear primero un objeto en el def que contenga los datos
    # for producto in productos:
    #      producto.descuento_subscriptor = 10
    #      producto.save()

    return render(request, 'core/productos.html',data)
