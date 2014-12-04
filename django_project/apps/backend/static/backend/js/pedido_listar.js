$(function() {
    generarTabla('/configuracion/ventas/pedido/json/', function(data) {
        cargarTabla('table', data);
    });
});

function armarFila(index, instancia) {
    fila = '<tr>'
    
    
    // Atributos
    fila += '<td> Pedido de Venta Nº : ' + (index + 1) + '</td>';	        
    
    if(false){
		fila += '<td><strong> Entregado </strong></td>';    	
    }else{
    	fila += '<td> <button type="button" class="btn btn-default">Marcar como Entregado</button> </td>';
    }
    // Botones 'Editar' y 'Eliminar'
    fila += '<td>' +
            ' <a href="/configuracion/ventas/pedido/' + instancia.pk + '/' +
            '" class="btn btn-info" title="Ver"><span class="glyphicon glyphicon-eye-open"></span></a>' +
            ' <a href="/configuracion/ventas/pedido/' + instancia.pk + '/editar/' +
            '" class="btn btn-primary" title="Editar"><span class="glyphicon glyphicon-pencil"></span></a>' +
            ' <button type="button" class="modal-eliminar btn btn-danger" data-toggle="modal" data-target="#modal-eliminar" ' +
            'data-id="' + instancia.pk + '" title="Eliminar"><span class="glyphicon glyphicon-trash"></span></button>' +
            '</td>';
    
    fila += '</tr>';
    
    return fila;
}

$(document).on("click", ".modal-eliminar", function () {
     var pk = $(this).data('id');
     $("#confirmar-eliminar").attr('href', $("#confirmar-eliminar").attr('href').replace(0, pk));
});

    