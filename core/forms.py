from django import forms
from django.forms import ModelForm, fields
from .models import Producto, CategoriaProducto
from django.forms.widgets import ClearableFileInput

form_file = {'class': 'form-control-file form-control form-control-sm', 'title': 'Debe subir una imagen'}
form_select = {'class':'form-select form-contro form-control-sm'}
form_text_area = {'class': 'form-control form-control-sm', 'rows': 2, 'placeholder':'Ingrese una descripcion'}
form_control = {'class': 'form-control form-control-sm', 'placeholder':'Ingrese el Nombre del Producto'}
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
            'nombreProducto': forms.TextInput(attrs=form_control),
            'descripcionProducto': forms.Textarea(attrs=form_text_area),
            'precioProducto': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': '$ 45.000'}),
            'descuento_subscriptor': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'min': 1, 'max': 100}),
            'descuento_oferta': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'min': 1, 'max': 100,}),
            'cantidadProducto': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'disponibilidadProducto': forms.Select(attrs=form_select),
            'imagenProducto' : forms.FileInput(attrs=form_file),
            'categoriaProducto' : forms.Select(attrs=form_select),
        } 

