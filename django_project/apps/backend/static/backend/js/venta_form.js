var total = 0;
var id_domicilio = 0;
var new_domicilio = false;

$(function(){
  numero_factura();
  precio_detalle();
  $("#id_total").prop("readonly", true);
  validarPisoDepartamento();
});

$(function(){
  $("#find_all_clientes").on("click",function(){
    show_mini_loading_cliente();
    clear_campos_seleccionar_cliente();
    cargarListadoClientes();
  });
  $("#find_clientes").on("click",function(){
    show_mini_loading_cliente();
    cargarListadoClientes();
  });
  $(document).on('click', '.list-group-item',function(){
    $("#listado_clientes").find(".active").removeClass("active");
    $(this).addClass("active");
    $(this).find("input").prop('checked', true);
  });
  $("#btn_show_modal_clientes").on("click",function(){
    show_mini_loading_cliente();
    $("#modal-select-cliente").modal('show');
    clear_campos_seleccionar_cliente();
    cargarListadoClientes();
  });
  $("#seleccionar_cliente_modal").on("click",function(){
  	if($('input[name="listado_clientes"]:checked').val() > 0){
	  	$("#modal-select-cliente").modal('hide');
	  	showMiniLoading();
	  	$("#id_cliente").val($('input[name="listado_clientes"]:checked').val());
	  	cargarCliente($('input[name="listado_clientes"]:checked').val());
  	}else{
  		alert("Debe seleccionar un Cliente");
  	}
  });
  $("#use_domicilio_cliente").on("click",function(){
    showMiniLoading();
    $("#id_domicilio").val(id_domicilio);
    cargarDomicilioCliente();
  });
  $("#nuevo_domicilio").on("submit",function(e){
  	e.preventDefault();
  	var jqxhr = $.ajax({
                  type: "POST",
                  dataType: "json",
				  url: "/configuracion/domicilio/json/crear/",
				  data:$(this).serialize()
		})
	  .done(function(data) {
	    $("#domicilio_calle").text(data[0].fields.calle);
        $("#domicilio_numero").text(data[0].fields.numero);
        $("#domicilio_piso").text(data[0].fields.piso);
        $("#domicilio_departamento").text(data[0].fields.departamento);
        $("#domicilio_localidad").text(data[0].fields.localidad);
        $("#domicilio_provincia").text(data[0].fields.provincia);
        validarPisoDepartamento();
        $("#id_domicilio").append('<option value="'+ data[0].pk +'">Nuevo Domicilio</option>');
        $("#id_domicilio").val(data[0].pk);
        new_domicilio = true;
	  })
	  .fail(function() {
	    alert( "error" );
	  });
  });
  $("#btn-modal-new-direccion").on("click",function(){
  	$("#nuevo_domicilio").trigger("reset");
  	$("#modal-new-direccion").modal('show');
  });
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


function cargarListadoClientes(){
  var param_nombre = $("#buscar_cliente_nombre").val();
  var param_apellido = $("#buscar_cliente_apellido").val();	
  $("#listado_clientes").empty();
  $.getJSON('/configuracion/ventas/cliente/json/?nombre=' + param_nombre + '&apellido=' + param_apellido, function(data) {
    $.each(data,function(index, item){
      $("#listado_clientes").append('<li class="list-group-item">' +
          '<div class="radio" style="margin-left: 40px;">'+
              '<input type="radio" name="listado_clientes" value="'+item.pk+'">' +
              item.fields.nombre + " " +item.fields.apellido +
          '</div>'+
        '</li>'
      );
    });
    hide_mini_loading_cliente();
  });
}

function cargarCliente(id_cliente){
   
   $.getJSON('/configuracion/ventas/cliente/json/'+ id_cliente, function(data) {
   	$("#cliente_nombre").text(data[0].fields.nombre);
   	$("#cliente_apellido").text(data[0].fields.apellido);
   	$("#cliente_telefono").text(data[0].fields.telefono);
   	if(!new_domicilio){
	   	if(data[0].fields.domicilio){
	   		$("#use_domicilio_cliente").show();
	   		id_domicilio = data[0].fields.domicilio;
	   	}else{
	   		$("#use_domicilio_cliente").hide();
	   		$("#id_domicilio").val("");
            clearDomicilioCliente();
	   	}
   	}else{
   	   if(data[0].fields.domicilio){
	   		$("#use_domicilio_cliente").show();
	   	}else{
	   		$("#use_domicilio_cliente").hide();
	   	}
   	}
    hideMiniLoading();
  });
}
function cargarDomicilioCliente(){
   $.getJSON('/configuracion/domicilio/json/'+ id_domicilio, function(data) {
     $("#domicilio_calle").text(data[0].fields.calle);
     $("#domicilio_numero").text(data[0].fields.numero);
     $("#domicilio_piso").text(data[0].fields.piso);
     $("#domicilio_departamento").text(data[0].fields.departamento);
     $("#domicilio_localidad").text(data[0].fields.localidad);
     $("#domicilio_provincia").text(data[0].fields.provincia);
     validarPisoDepartamento();
     hideMiniLoading();
  });
}

function clearDomicilioCliente(){
  $("#domicilio_calle").text("");
  $("#domicilio_numero").text("");
  $("#domicilio_piso").text("");
  $("#domicilio_departamento").text("");
  $("#domicilio_localidad").text("");
  $("#domicilio_provincia").text("");
  validarPisoDepartamento();
}

function validarPisoDepartamento(){
	if($("#domicilio_piso").text() == 0){
		$("#row_domicilio_piso_departamento").hide();
	}else{
		$("#row_domicilio_piso_departamento").show();
	}
}
function clear_campos_seleccionar_cliente(){
	$("#buscar_cliente_nombre").val("");
	$("#buscar_cliente_apellido").val("");
}
function show_mini_loading_cliente(){
    $("#modal-select-cliente").find(".spinner_modal").show();
}
function hide_mini_loading_cliente(){
  setTimeout(function(){
                        $("#modal-select-cliente").find(".spinner_modal").hide();
                        }
            , 5000);

}

    