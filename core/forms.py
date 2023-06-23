from django import forms
from django.forms import ModelForm, fields
from .models import Producto, Categoria
from django.forms.widgets import ClearableFileInput

form_file = {'class': 'form-control-file form-control form-control-sm', 'title': 'Debe subir una imagen'}
form_select = {'class':'form-select form-control form-control-sm'}
form_text_area = {'class': 'form-control form-control-sm', 'rows': 2, 'placeholder':'Ingrese una descripcion'}
form_control = {'class': 'form-control form-control-sm', 'placeholder':'Ingrese el Nombre del Producto'}
form_precio = {'class':'form-control', 'placeholder':'Ingrese el precio'}
form_desc = {'class': 'form-control', 'placeholder':'3%'}
form_descOferta = {'class': 'form-control', 'placeholder':'5%'}

class ProductoForm(ModelForm):
    



    class Meta:
        model = Producto
        fields = [
                  'nombre', 
                  'descripcion', 
                  'precio', 
                  'descuento_subscriptor',
                  'descuento_oferta', 
                  'imagen', 
                  'categoria', 
                  ]

        widgets = {
            'nombre': forms.TextInput(attrs=form_control),
            'descripcion': forms.Textarea(attrs=form_text_area),
            'precio': forms.NumberInput(attrs=form_precio),
            'descuento_subscriptor': forms.NumberInput(attrs=form_desc),
            'descuento_oferta': forms.NumberInput(attrs=form_descOferta),
            'imagen' : forms.FileInput(attrs=form_file),
            'categoria' : forms.Select(attrs=form_select),
        } 

