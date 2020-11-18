$('.like').click(function(){
    var likeIcon = $(this).find('img')
    var likeCounter = $(this).parent().find('.like_counter')
    $.ajax({
            url: 'like/'+$(this).attr('name')+'/',
            type: 'get',
            success: function(response){
              likeIcon.attr('src', likeIcon.attr('src') === '/static/images/icons/like_unset.png'
               ? '/static/images/icons/like_set.png'
               : '/static/images/icons/like_unset.png')
              likeCounter.text(response.likes);
            },
            error: function(rs, r){
              alert("Произошла ошибка");
            }
    })
});