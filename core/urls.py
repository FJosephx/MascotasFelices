from django.urls import path
from .views import index, registro,nosotros


urlpatterns = [
    path('', index, name="index"),
    path('registro', registro, name="registro"),
    path('nosotros', nosotros, name="nosotros"),
    # path('poblar_bd', poblar_bd, name="poblar_bd"),
    # path('vehiculo/<action>/<id>', vehiculo, name="vehiculo"),
    # path('vehiculo_tienda', vehiculo_tienda, name="vehiculo_tienda"),
    # path('vehiculo_ficha/<id>', vehiculo_ficha, name="vehiculo_ficha"),
]
