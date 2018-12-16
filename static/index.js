$('#create').click(function () {
    var _name = $("#board_name").val();
    var _about = $("#board_about").val();

    $.ajax({
        type: "POST",
        contentType: "application/json; charset=utf-8",
        url: '/create_board',
        data: JSON.stringify({ name: _name, about: _about}),
        success: function (data) {
            window.location.replace("/board/" + data.id);
        },
        dataType: "json"
    });

    console.log("asdf");
    
});