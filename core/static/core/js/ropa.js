
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
  
  
  
  });