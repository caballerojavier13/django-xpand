var miniLoading = false;

$(function() {
    if ($("#desplegable li").length < 1) {
        $("#desplegable").parent().remove();
    }
    $(".alert .close").on("click", function() {
        $(".alert").hide();
    });
    $(".volver").on("click", function() {
        window.history.back();
    });
    $("label").addClass("col-xs-3 col-sm-3 col-md-2 control-label");
    $(".form-group div select").addClass("form-control");
    $(".form-group li input").addClass("col-xs-12 col-sm-9 col-md-8");
    fn_money();
});


function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

function getURL_Id() {
    var urlAux = window.location.pathname.split("/")
    return urlAux[urlAux.length - 2];
}

function showMiniLoading() {
    miniLoading = true;
    $("body").append('<svg class="spinner" id="mini_loading" width="65px" height="65px" viewBox="0 0 66 66" xmlns="http://www.w3.org/2000/svg"><circle class="path" fill="none" stroke-width="3" stroke-linecap="round" cx="33" cy="33" r="30"></circle></svg>');
}

function hideMiniLoading() {
    if(miniLoading) {
        setTimeout(
            function() {
                $("#mini_loading").remove();
            }, 2000);
    }
}

function fn_money(){
  $(".money").each(function(index,item){
    $(item).text("$ " + parseFloat($(item).text().replace(',', '.')).toFixed(2));
  });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});
