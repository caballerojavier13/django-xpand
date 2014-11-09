function cargarTabla(idTabla, data, callback) {
    $(idTabla + " tbody").empty();
    if (data.length > 0) {
        $.each(data, function(index, elemento) {
            $(idTabla + " tbody").append(elemento);
        });
    }
    else {
        tablaVacia(idTabla, "100%");
    }
	if (callback) {
	    callback();
	}
}

function generarTabla(url, callback){
    var tabla = new Array();
    $.getJSON(url, function(data) {
	    $.each(data, function(index, elemento) {
	        var fila = armarFila(index, elemento);
	        tabla.push(fila);
	    });
	    callback(tabla);
	});
}

function tablaVacia(idTabla, cantidadColumnas){
    $(idTabla + " tbody").html('<tr><td class="text-center" colspan="'+ cantidadColumnas +'">No se ha encontrado ningún elemento.</td></tr>');
}