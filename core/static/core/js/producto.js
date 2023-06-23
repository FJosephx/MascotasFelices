$(document).ready(function(){



    $.validator.setDefaults({
        messages: {
          required: "Este campo es obligatorio",
        },
    });

    $('#formulario').validate({ 
        rules: {

            



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
                digits: true,
                number: true,
                range: [0, 100],

             },
            'descuento_oferta': {
                required: true,
                digits: true,
                number: true,
                range: [0, 100],

             },

        },
        messages: {

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
                required: 'Debe Ingresar el Desc. Subscriptor',
                number: 'Debe ingresar un número',
                digits: 'Debe ingresar un número entero',
                
                range: 'El descuento debe ser un número entre 0 y 100',


            },
            
            'descuento_oferta': {
                required: 'Debe ingresar un Desc. en Oferta',
                number: 'Debe ingresar un número',
                digits: 'Debe ingresar un número entero',
                
                range: 'El descuento debe ser un número entre 0 y 100',


            },


        },
        

        errorPlacement: function(error, element) {
            
            error.insertAfter(element); // Inserta el mensaje de error después del elemento
            // element.addClass('is-invalid');
            error.addClass('div invalid-feedback fw-bolder'); // Aplica una clase al mensaje de error


        },
        


    });
  
  });