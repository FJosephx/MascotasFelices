from django import forms
from django.forms import ModelForm, fields
from .models import Producto, CategoriaProducto
from django.forms.widgets import ClearableFileInput



class ProductoForm(ModelForm):



    class Meta:
        model = Producto
        fields = [
                  'nombreProducto', 
                  'descripcionProducto', 
                  'precioProducto', 
                  'descuento_subscriptor',
                  'descuento_oferta', 
                  'imagenProducto', 
                  'categoriaProducto', 
                  'disponibilidadProducto',
                  'cantidadProducto'
                  ]

        widgets = {
            'nombreProducto': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ingrese el Nombre del producto'}),
            'descripcionProducto': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 2, 'placeholder': 'Ingrese una descripcion breve del producto'}),
            'precioProducto': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': '$ 45.000'}),
            'descuento_subscriptor': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'min': 1, 'max': 100}),
            'descuento_oferta': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'min': 1, 'max': 100,}),
            'cantidadProducto': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'disponibilidadProducto': forms.Select(attrs={'class': 'form-select form-control-sm'}),


        } 

