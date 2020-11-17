$(document).ready(function(){
    $(".like").click(function(){
        $.ajax({
            url: "",
            type: "GET",
            data: {
                button_text: $(this).text()
            },
            success: function(response) {
                $.(".like").text(response.seconds)
            }
        });
    });

});