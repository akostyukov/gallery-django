$('.like').click(function(){
    var likeIcon = $(this).find('img')
    var likeCounter = $(this).parent().find('.like_counter')
    $.ajax({
            url: 'like/'+$(this).attr('name')+'/',
            type: 'get',
            success: function(response){
              likeIcon.attr('src', response.image_url);
              likeCounter.text(response.likes);
            },
            error: function(rs, r){
              alert("Произошла ошибка");
            }
    })
});