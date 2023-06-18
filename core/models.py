from django.core.validators import MinValueValidator, MaxValueValidator
import locale
from django.db import models


# Create your models here
class CategoriaProducto(models.Model):
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de la categoría")
    def __str__(self):
        return self.nombreCategoria
    


# Create Modelo para Productos
class Producto(models.Model):

    DISPONIBILIDAD_CHOICES = (
        ('1', 'Disponible en bodega'),
        ('2', 'Agotado'),
        ('3', 'En oferta'),
    )

    disponibilidadProducto = models.CharField(max_length=1, choices=DISPONIBILIDAD_CHOICES, verbose_name="Disponibilidad Producto")


    nombreProducto = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre Producto")
    descripcionProducto = models.CharField(max_length=80, null=True, blank=True, verbose_name="Descripcion Producto")

    precioProducto = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Precio Producto")
    descSubscriptor = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="Desc. Subscriptor")
    descuento_oferta = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="Descuento Oferta")

    imagenProducto = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen Producto")
    

    categoriaProducto = models.ForeignKey(CategoriaProducto, on_delete=models.DO_NOTHING, verbose_name="Categoria Producto")


    def __str__(self):
        return self.nombreProducto

