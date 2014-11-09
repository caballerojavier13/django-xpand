$(function() {
    generarTabla('/app/persona/json/', function(data) {
        cargarTabla('table', data);
    });
});

function armarFila(index, instancia) {
    fila = '<tr>'
    
    // Atributos
    fila += '<td>' + instancia.pk + '</td>' +
'<td>' + instancia.fields.dni + '</td>'
 + '<td>' + instancia.fields.nombre + '</td>'
 + '<td>' + instancia.fields.apellido + '</td>'
;
    
    
    // Asociaciones
    fila += '<td>' + '<a href="/app/domicilio/' + instancia.fields.domicilio + '/' +
'" class="btn btn-info">Ver domicilio</a>' + '</td>'
;
    
    
    // Botones 'Editar' y 'Eliminar'
    fila += '<td>' +
            '<a href="/app/persona/' + instancia.pk + '/editar/' +
            '" class="btn btn-primary" title="Editar"><span class="glyphicon glyphicon-pencil"></span></a>' +
            '<button type="button" class="modal-eliminar btn btn-danger" data-toggle="modal" data-target="#modal-eliminar" ' +
            'data-id="' + instancia.pk + '" title="Eliminar"><span class="glyphicon glyphicon-trash"></span></button>' +
            '</td>';
    
    fila += '</tr>';
    
    return fila;
}

$(document).on("click", ".modal-eliminar", function () {
     var pk = $(this).data('id');
     $("#confirmar-eliminar").attr('href', $("#confirmar-eliminar").attr('href').replace(0, pk));
});

    