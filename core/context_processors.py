from .models import Carrito

def registrar_carrito(request):

    mostrar_carrito = False
    cantidad_productos = 0
    


        
   
    return {
        'mostrar_carrito': mostrar_carrito,
        'cantidad_productos': cantidad_productos,
    }