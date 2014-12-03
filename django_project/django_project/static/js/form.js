$(function(){
    $(".datepicker").prop('readonly', true);
    var input = $('.datepicker').parent().html();
    var parent = $('.datepicker').parent();
    $('.datepicker').remove();
    parent.append('<div class="input-group">'+
    input +
    '<span class="input-group-addon glyphicon glyphicon-calendar" style="top:0px;"></span></div>');
    $('.datepicker').datepicker({
      format: "dd/mm/yyyy"
    });
});
