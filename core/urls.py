from django.urls import path
from .views import cambiar_estado_boleta, poblar,obtener_productos,eliminar_producto_en_bodega,salir,admin_productos,ventas, usuarios,home, ropa, ficha, misdatos, nosotros, registro, iniciar_sesion, administracion, bodega, boleta, miscompras, carrito


urlpatterns = [
    
    path('', home, name='home'),
    path('ropa', ropa, name='ropa'),
    path('ficha/<producto_id>', ficha, name='ficha'),
    path('registro', registro, name='registro'),
    path('iniciar_sesion', iniciar_sesion, name='iniciar_sesion'),
    path('administracion', administracion, name='administracion'),
    path('bodega', bodega, name="bodega"),
    path('boleta', boleta, name='boleta'),
    path('carrito', carrito, name="carrito"),
    path('miscompras', miscompras, name="miscompras"),
    # path('misdatos', misdatos, name="misdatos"),
    path('misdatos', misdatos, name="misdatos"),
    path('nosotros', nosotros, name="nosotros"),
    path('usuarios', usuarios, name="usuarios"),
    # path('productos', productos, name="productos"),
    path('admin_productos/<accion>/<id>', admin_productos, name="admin_productos"),

    path('ventas', ventas, name="ventas"),
    path('poblar', poblar, name='poblar'),
    path('salir', salir, name='salir'),
    path('obtener_productos', obtener_productos, name='obtener_productos'),
path('ventas', ventas, name='ventas'),
    path('boleta/<nro_boleta>', boleta, name='boleta'),
    path('cambiar_estado_boleta/<nro_boleta>/<estado>', cambiar_estado_boleta, name='cambiar_estado_boleta'),
    path('eliminar_producto_en_bodega/<bodega_id>', eliminar_producto_en_bodega, name='eliminar_producto_en_bodega'),

]
