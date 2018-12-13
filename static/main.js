$(".text-owner").click(function (e) {
    var parentOffset = $(this).parent().offset();
    var position = {
        x: (e.pageX - parentOffset.left),
        y: (e.pageY - parentOffset.top)
    }

    console.log(position);
});

//scrolling detection
$(window).scroll(function () {
    console.log("scrolling");
    if ($(window).scrollTop() + $(window).height() == $(document).height()) {
        console.log("typpi");

    }
});

$('#submit-btn').click(function () {
    console.log("asdf");
    var _name = $("#name").val();
    var _msg = $("#msg").val();

    $.ajax({
        type: "POST",
        contentType: "application/json; charset=utf-8",
        url: "/add_msg",
        data: JSON.stringify({ name: _name, msg: _msg }),
        success: function (data) {
            console.log("Success!")
        },
        dataType: "json"
    });
});