$(document).ready(function(){
    $('.comments').click(function(){
        var commentsField = $(this).find('.comments-block')
        $.ajax({
                url: $(this).attr('name')+'/',
                type: 'get',
                success: function(response){
                  comments.text(response.comments)
                },
                error: function(rs, r){
                  alert("Произошла ошибка");
                }
        });
    });
});