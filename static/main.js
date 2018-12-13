$(".text-owner").click(function(e){
    var parentOffset = $(this).parent().offset();
    var position = {
        x: (e.pageX - parentOffset.left),
        y: (e.pageY - parentOffset.top)
    }

    console.log(position);
    
 });