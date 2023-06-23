from django.shortcuts import render, redirect
from .models import Categoria, Producto, Boleta, Carrito, DetalleBoleta, Bodega, Perfil
from .forms import ProductoForm
# , BodegaForm, RegistroClienteForm, IngresarForm
import locale
from core.templatetags.custom_filters import formatear_dinero, formatear_numero



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

    if request.method == 'POST':
        buscar = request.POST.get('buscar')
        registros = Producto.objects.filter(nombre__icontains=buscar).order_by('nombre')
    else:
        registros = Producto.objects.all().order_by('nombre')

    productos = []
    
    for registro in registros:
        productos.append(obtener_info_producto(registro.id))

    data = { 
        'productos': productos,
        'titulo': 'Mascotas Felices', 
        }
    
    return render(request, 'core/index.html', data)
     

    
    # resultado=''
     
    # list = Producto.objects.all().order_by('nombre')
    # if request.method == 'POST':
    #     buscar = request.POST.get('buscar')
    #     if buscar.strip() != '':
    #         resultado = buscar
    #         list = Producto.objects.filter(nombre__icontains=buscar).order_by('nombre')
             
    # data = { 
    #     'titulo': 'Mascotas Felices', 
    #     'list': list,
    #     'resultado': resultado
    # }

    # return render(request, 'core/index.html', data)


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


def obtener_info_producto(producto_id):

    producto = Producto.objects.get(id=producto_id)
    stock = Bodega.objects.filter(producto_id=producto_id).exclude(detalleboleta__isnull=False).count()
    
    # Preparar texto para mostrar estado: en oferta, sin oferta y agotado
    con_oferta = f'<span class="text-primary"> EN OFERTA {producto.descuento_oferta}% DE DESCUENTO </span>'
    sin_oferta = '<span class="text-success"> DISPONIBLE EN BODEGA </span>'
    agotado = '<span class="text-danger"> AGOTADO </span>'

    if stock == 0:
        estado = agotado
    else:
        estado = sin_oferta if producto.descuento_oferta == 0 else con_oferta

    # Preparar texto para indicar cantidad de productos en stock
    # en_stock = f'En stock: {formatear_numero(stock)} {"unidad" if stock == 1 else "unidades"}'
    en_stock = f'<div class="d-flex justify-content-between"><span>En stock: </span> <span> {formatear_numero(stock)} {"unidad" if stock == 1 else "unidades"} </span></div>'

    return {
        'id': producto.id,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'imagen': producto.imagen,
        'html_estado': estado,
        'html_precio': obtener_html_precios_producto(producto),
        'html_stock': en_stock,
    }
def calcular_precios_producto(producto):
    precio_normal = producto.precio
    precio_oferta = producto.precio * (100 - producto.descuento_oferta) / 100
    precio_subscr = producto.precio * (100 - (producto.descuento_oferta + producto.descuento_subscriptor)) / 100
    hay_desc_oferta = producto.descuento_oferta > 0
    hay_desc_subscr = producto.descuento_subscriptor > 0
    return precio_normal, precio_oferta, precio_subscr, hay_desc_oferta, hay_desc_subscr

def obtener_html_precios_producto(producto):
    
    precio_normal, precio_oferta, precio_subscr, hay_desc_oferta, hay_desc_subscr = calcular_precios_producto(producto)
    
    normal = f'<div class="d-flex justify-content-between"><span>Normal:</span> <span>{formatear_dinero(precio_normal)}</span></div>'
    tachar = f'<div class="d-flex justify-content-between"><span>Normal:</span> <span class="text-decoration-line-through"> {formatear_dinero(precio_normal)} </span></div>'
    oferta = f'<div class="d-flex justify-content-between"><span>Oferta:</span> <span class="text-success"> {formatear_dinero(precio_oferta)} </span></div>'
    subscr = f'<div class="d-flex justify-content-between"><span>Subscrito:</span> <span class="text-danger"> {formatear_dinero(precio_subscr)} </span></div>'

    if hay_desc_oferta > 0:
        texto_precio = f'{tachar}{oferta}'
    else:
        texto_precio = normal

    if hay_desc_subscr > 0:
        texto_precio += f'{subscr}'

    return texto_precio