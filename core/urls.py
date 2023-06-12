from django.urls import path
from .views import productos,ventas, usuarios,home, ropa, ficha, misdatos, nosotros, registro, login, administracion, bodega, boleta, miscompras, carrito


urlpatterns = [
    path('', home, name='home'),
    path('ropa', ropa, name='ropa'),
    path('ficha/<id>', ficha, name='ficha'),
    path('registro', registro, name='registro'),
    path('login', login, name='login'),
    path('administracion', administracion, name='administracion'),
    path('bodega', bodega, name="bodega"),
    path('boleta', boleta, name='boleta'),
    path('carrito', carrito, name="carrito"),
    path('miscompras', miscompras, name="miscompras"),
    path('misdatos', misdatos, name="misdatos"),
    path('nosotros', nosotros, name="nosotros"),
    path('usuarios', usuarios, name="usuarios"),
    # path('productos', productos, name="productos"),
    path('productos/<action>/<id>', productos, name="productos"),

    path('ventas', ventas, name="ventas"),



]
