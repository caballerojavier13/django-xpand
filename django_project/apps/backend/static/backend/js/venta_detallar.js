
$(function(){
  fecha_day();
  fecha_month();
  numero_factura();
});


function fecha_day(){
  var day = $(".fecha_day").text();
  if(day < 10){
    day = "0" + day;
    $(".fecha_day").text(day);
  }
}

function fecha_month(){
  var month = $(".fecha_month").text();
  if(month < 10){
    month = "0" + month;
    $(".fecha_month").text(month);
  }
}

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


    