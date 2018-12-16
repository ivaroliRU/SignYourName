var pos = {x: 0, y: 0};
var isShowingForm = false;
var isOverForm = false;

$(".text-owner").click(function (e) {
    var parentOffset = $(this).parent().offset();

    pos.x = (e.pageX - parentOffset.left),
    pos.y = (e.pageY - parentOffset.top)

    if(!isShowingForm && !isOverForm){
        $("#msg-form").css('left', pos.x + 'px');
        $("#msg-form").css('top', pos.y + 'px');
        $("#msg-form").show();
    }
});

//scrolling detection
$(window).scroll(function () {
    console.log("scrolling");
    if ($(window).scrollTop() + $(window).height() == $(document).height()) {
    }
});


$('#cancel-btn').click(function () {
    clear_form();
});

$('#submit-btn').click(function () {
    var _name = $("#name").val();
    var _msg = $("#msg").val();
    var pathname = window.location.pathname+'/add_msg';

    $.ajax({
        type: "POST",
        contentType: "application/json; charset=utf-8",
        url: pathname,
        data: JSON.stringify({ name: _name, msg: _msg , position: pos}),
        success: function (data) {
            add_text(_name, _msg, pos);
            clear_form();
        },
        dataType: "json"
    });
});

$("#msg-form").mouseenter(function(){
    isOverForm = true;
    console.log("entering");
}).mouseleave(function(){
    isOverForm = false;
    console.log("leaving");
});

function clear_form(){
    $("#msg-form").hide();
    $("#msg").val("");
    $("#name").val("");
}

function add_text(name, msg, position){
    $(".text-owner").append('<div style="position:absolute; left:'+position.x+'px; top:'+position.y+'px;"><div>'+ name +':</div><div>'+ msg +'</div>');
}