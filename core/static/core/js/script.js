

document.addEventListener('DOMContentLoaded',function(event){



  $('#generarContrasena').click(function() {
    $('#passwordgenerate').val('Duoc@2023');
  });

  console.log("Código de JavaScript de Bootstrap ejecutándose...");

  function generarCodigoAleatorio() {
    var codigo = Math.floor(Math.random() * 10000) + 1;
    return codigo;
  }

  const copyEmailBtn = document.querySelector('#copy-email');

  copyEmailBtn.addEventListener('click', () => {
  const email = generarCodigoAleatorio();

  // Copiar el email al portapapeles
  navigator.clipboard.writeText(email)
    .then(() => {
      // Cambiar el texto del botón
      copyEmailBtn.innerText = 'Codigo de Descuento Copiado!';
    })
    .catch(err => {
      console.error('No se pudo copiar el Codigo de Descuento: ', err);
    });
  });




});


$(document).ready(function(){

  // funcion obtener datos api fakestore
  $.get('https://fakestoreapi.com/products',
  
  function(datos) 
  {   
      $('#tabla-ropas tbody').empty();
      $.each(datos, function(i, item) {
          
          var fila = '';
          fila += '<tr>' ;
          fila += '<td>' + item.title + '</td>';
          fila += '<td>' + item.description + '</td>';
          fila += '<td>' + item.price + '</td>';
          fila += '<td><img style="height: 50px" src="'+ item.image +'"></td>';

          fila += '</tr>';

          $('#tabla-ropas').append(fila);
      });
  });

  // funcion carrusel
  $('.slick-carousel').slick({
    // opciones de configuración de Slick
    dots: true,
    infinite: false,
    speed: 300,
    slidesToShow: 3,
    slidesToScroll: 4,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
  ]
  });

  // nombrando la clase que usara slick
  $('.single-item').slick();


});


