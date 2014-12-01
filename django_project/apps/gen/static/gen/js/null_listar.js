$(function() {
    generarTabla('/app//json/', function(data) {
        cargarTabla('table', data);
    });
});

function armarFila(index, instancia) {
    fila = '<tr>'
    
    // Atributos
    fila += '<td>' + instancia.pk + '</td>' +
'<td>' + instancia.fields.nombre + '</td>'
;
    
    
    // Asociaciones
    fila += '<td>' +
            '<div class="dropdown">' +
            '<button class="btn btn-info" type="button" data-toggle="dropdown" aria-haspopup="true" role="button" aria-expanded="false">' +
            'Relaciones <span class="caret"></span>' +
            '</button>' +
            '<ul class="dropdown-menu" role="menu" aria-labelledby="dLabel">';
    
if (instancia.fields.refEmpresa != null) {
    fila += '<li role="presentation"><a role="menuitem" tabindex="-1" href="/app/refEmpresa/' + instancia.fields.refEmpresa + '/' +
'">RefEmpresa</a></li>'
;
}
else {
    fila += '<li class="disabled" role="presentation"><a role="menuitem" tabindex="-1" href="#">Sin refEmpresa</a></li>'
;
}
if (instancia.fields.refDomicilio != null) {
    fila += '<li role="presentation"><a role="menuitem" tabindex="-1" href="/app/refDomicilio/' + instancia.fields.refDomicilio + '/' +
'">RefDomicilio</a></li>'
;
}
else {
    fila += '<li class="disabled" role="presentation"><a role="menuitem" tabindex="-1" href="#">Sin refDomicilio</a></li>'
;
}
    
    fila += '</ul>' +
            '</div>' +
            '</td>';
    
    
    // Botones 'Editar' y 'Eliminar'
    fila += '<td>' +
            ' <a href="/app//' + instancia.pk + '/' +
            '" class="btn btn-info" title="Ver"><span class="glyphicon glyphicon-eye-open"></span></a>' +
            ' <a href="/app//' + instancia.pk + '/editar/' +
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

    