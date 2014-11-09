function cargarTabla(idTabla, data, callback){
	$(idTabla + " tbody").empty();
  if(data.length > 0){
    $.each(data,function(index, element){
      $(idTabla + " tbody").append(element);
    });  
  }else{
   tablaVacia(idTabla , 5); 
  }
	if(callback){
		callback();
	}
}

function getTabla(url, callback){
	var tabla = new Array();
	$.getJSON(url, function(data){
		jQuery.each(data,function(index, element){
			var item = addFila(index, element);
			tabla.push(item);
		});
		callback(tabla);
	});
}

function tablaVacia(idtabla, cant_col){
  $(idtabla + " tbody").html('<tr><td class="text-center" colspan="'+ cant_col +'">No se ha encontrado ningún elemento.</td></tr>');
}
