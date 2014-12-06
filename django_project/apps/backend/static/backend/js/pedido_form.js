var total = 0;

$(function(){
  numero_factura();
  precio_detalle();
  $("#id_total").prop("readonly", true);
  cargarListado();
});



function numero_factura(){

  var numero = $("#numero_factura").text();

  if(numero < 100000){
    numero = "0" + numero;
    if(numero < 10000){
      numero = "0" + numero
      if(numero < 1000){
        numero = "0" + numero
        if(numero < 100){
          numero = "0" + numero
          if(numero < 10){
            numero = "0" + numero
            $("#numero_factura").text(numero);
          }else{
            $("#numero_factura").text(numero);
          }
        }else{
          $("#numero_factura").text(numero);
        }
      }else{
        $("#numero_factura").text(numero);
      }
    }else{
      $("#numero_factura").text(numero);
    }
  }

}


function precio_detalle(){
  $(".table-detalle tbody tr").each(function(index,item){
    $(item).find("td:nth-child(3)").text("$ " + parseFloat($(item).find("td:nth-child(3)").text().replace(',', '.')).toFixed(2));
    var valor = parseFloat($(item).find("td:nth-child(3)").text().slice(2) * $(item).find("td:nth-child(1)").text()).toFixed(2);
    $(item).find("td:nth-child(4)").text("$ " + valor);
    total = parseFloat(valor) + parseFloat(total);
  });
  fn_total();
}

function fn_total(){
  if($.isNumeric( total )) {
    $("#id_total").val(parseFloat(total).toFixed(2));
  }else{
    $("#id_total").val("0.00");
  }
}


function cargarListado(){
  $("#listado_clientes").empty();
  $.getJSON('/configuracion/ventas/cliente/json/', function(data) {
    $.each(data,function(index, item){
      $("#listado_clientes").append('<li class="list-group-item">' +
          '<div class="radio" style="margin-left: 40px;">'+
              '<input type="radio" name="optionsRadios" value="option1">' +
              item.fields.nombre + " " +item.fields.apellido +
          '</div>'+
        '</li>'
      );
    });
  });
}

    