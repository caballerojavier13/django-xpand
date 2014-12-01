$(function(){
  altoForm();
  $(window).resize(function() {
    altoForm();
  });
});


function altoForm(){
  var window_height = $( window ).height();
  var header = $("body header").css("height");
  var footer = $("body footer").css("height");
  var inner_container_margin = parseInt($(".inner-container").css("margin-top")) + parseInt($(".inner-container").css("margin-bottom"));
  var total = parseInt(window_height) - parseInt(header) - parseInt(footer) - inner_container_margin - 70;
  if(parseInt($(".inner-container form").css("height"))  < total){
      $(".inner-container").css("height",parseInt(total));
  }
  centrarForm();
}

function centrarForm(){
  var top = parseInt($(".inner-container").css("height")) - parseInt($(".inner-container form").css("height"));
  $(".inner-container form").css("top", parseFloat(top / 2));
}
