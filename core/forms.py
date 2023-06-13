from django import forms
from django.forms import ModelForm, fields
from .models import Producto, CategoriaProducto
from django.forms.widgets import ClearableFileInput



class ProductoForm(ModelForm):

    imagenProducto = forms.ImageField(
        label = "Imagen de Producto",
        required=False,
        widget=ClearableFileInput(attrs={"class": "form-control form-control-sm"}),
    )

    


    categoriaProducto = forms.ModelChoiceField(
        queryset=CategoriaProducto.objects.all(),
        empty_label=None,
        label="Categoría",

        widget=forms.Select(attrs={"class": "form-select form-control-sm"}),)
    

    class Meta:
        model = Producto
        fields = ['idProducto', 
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
            'idProducto': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ingrese el ID del producto'}),
            'nombreProducto': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ingrese el Nombre del producto'}),
            'descripcionProducto': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 2, 'placeholder': 'Ingrese una descripcion breve del producto'}),
            'precioProducto': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': '$ 45.000'}),
            'descuento_subscriptor': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'min': 1, 'max': 100}),
            'descuento_oferta': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'min': 1, 'max': 100,}),
            'cantidadProducto': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'disponibilidadProducto': forms.Select(attrs={'class': 'form-select form-control-sm'}),


        } 

