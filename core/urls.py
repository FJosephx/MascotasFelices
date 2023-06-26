from django.urls import path
from .views import obtener_productos,eliminar_producto_en_bodega,salir,admin_productos,ventas, usuarios,home, ropa, ficha, misdatos, nosotros, registro, inciar_sesion, administracion, bodega, boleta, miscompras, carrito


urlpatterns = [
    path('', home, name='home'),
    path('ropa', ropa, name='ropa'),
    path('ficha/<producto_id>', ficha, name='ficha'),
    path('registro', registro, name='registro'),
    path('inciar_sesion', inciar_sesion, name='inciar_sesion'),
    path('administracion', administracion, name='administracion'),
    path('bodega', bodega, name="bodega"),
    path('boleta', boleta, name='boleta'),
    path('carrito', carrito, name="carrito"),
    path('miscompras', miscompras, name="miscompras"),
    path('misdatos', misdatos, name="misdatos"),
    path('nosotros', nosotros, name="nosotros"),
    path('usuarios', usuarios, name="usuarios"),
    # path('productos', productos, name="productos"),
    path('admin_productos/<accion>/<id>', admin_productos, name="admin_productos"),

    path('ventas', ventas, name="ventas"),

    path('salir', salir, name='salir'),
    path('obtener_productos', obtener_productos, name='obtener_productos'),

    path('eliminar_producto_en_bodega/<bodega_id>', eliminar_producto_en_bodega, name='eliminar_producto_en_bodega'),

]
