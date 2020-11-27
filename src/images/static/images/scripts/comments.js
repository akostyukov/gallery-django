$(document).ready(function(){
    $('.add-comment').submit(function(){
        var commentsField = $(this).find('.comments-block')
        var form = $('.add-comment')
        $.ajax({
                url: 'add-comment/',
                type: form.attr('method'),
                data: form.serialize(),
                success: function(response){
                  $(".comments-block").append(`<b>${response.username}</b>: ${form.find('input[type="text"]').val()}<br>`)
                  form.find('input[type="text"]').val('')
                },
                error: function(rs, r){
                  alert("Произошла ошибка")
                }
        })
        return false
    })
    $.ajax({
            url: 'get-comments/',
            type: 'get',
            success: function(response){
               Object.keys(response.comments).forEach((key) => {
                    var {author, text} = response.comments[key]
                   $(".comments-block").append(`<b>${author}</b>: ${text}<br>`)
               })
            },
            error: function(rs, r){
              alert("Произошла ошибка")
            }
    })
})