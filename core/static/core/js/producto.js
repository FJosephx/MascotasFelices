$(document).ready(function(){
    console.log("hofa")

    $.validator.setDefaults({
        messages: {
          required: "Este campo es obligatorio",
        },
    });

    $('#formulario').validate({ 
        rules: {
            'cantidadProducto': {
                required: true,
                digits: true,
                number: true,
                range: [0, 1000],
            },
            'nombreProducto': {
                required: true,
                minlength: 2,
            },
            'descripcionProducto': {
                required: true,
                minlength: 2,
            },
            'precioProducto': {
                required: true,
                digits: true,
                number: true,
            },
            'imagenProducto': {
                required: true,
                // extension: "jpg|jpeg|png"
            },
            'categoriaProducto': {
                required: true,
            },
            'disponibilidadProducto': {
                required: true,
            },
            'descuento_subscriptor': {
                required: true,
                // digits: true,
                // number: true,
                // range: [0, 99],
            },
            'descuento_oferta': {
                required: true,
                // digits: true,
                // number: true,
                // range: [0, 99],
            },

        },
        messages: {
            'cantidadProducto': {
                required: 'Debe ingresar la cantidad del producto',
                range: 'Ingrese una cantidad del 1 al 1000'
            },
            'nombreProducto': {
                required: 'Debe ingresar el Nombre del Producto',
                minlength: 'Debe ingresar mas de 2 letras'
            },
            'descripcionProducto': {
                required: 'Debe ingresar la descripcion del Producto',
                minlength: 'Debe ingresar mas de 2 letras'
            },
            'precioProducto': {
                required: 'Debe ingresar el precio del producto',
                number: 'Debe ingresar un número',
                digits: 'Debe ingresar un número entero',
            },
            'imagenProducto': {
                required: 'Debe ingresar la imagen del producto',
                // extension: "Seleccione una imagen en formato JPG, JPEG, PNG"
            },
            'categoriaProducto': {
                required: 'Debe ingresar una categoria',
            },
            'disponibilidadProducto': {
                required: 'Debe ingresar una disponibilidad',
            },
            'descuento_subscriptor': {
                required: 'Debe ingresar descuento de subscriptor',
                // digits: 'Debe ingresar un numero entero',
                // number: 'Debe ingresar un numero',
                // range: 'Rango entre 1 y 99%',
            },
            'descuento_oferta': {
                required: 'Debe ingresar descuento de oferta',
                // digits: 'Debe ingresar un numero entero',
                // number: 'Debe ingresar un numero',
                // range: 'Rango entre 1 y 99%',
            },


        },
        errorPlacement: function(error, element) {
            error.insertAfter(element); // Inserta el mensaje de error después del elemento
            error.addClass('div alert alert-danger'); // Aplica una clase al mensaje de error
            element.after('<br>'); 
        },

    });
  
  });