$('.like').click(function(){
    var likeIcon = $(this).find('img')
    var likeCounter = $(this).parent().find('.like_counter')
    $.ajax({
            url: $(this).attr('name')+'/like/',
            type: 'get',
            success: function(response){
              if (likeIcon.attr('src') === '/static/images/icons/like_unset.png') {
                  likeIcon.attr('src', '/static/images/icons/like_set.png')
              } else {
                  likeIcon.attr('src', '/static/images/icons/like_unset.png')
              }
              likeCounter.text(response.likes)
            },
            error: function(rs, r){
              alert("Произошла ошибка")
            }
    })
});