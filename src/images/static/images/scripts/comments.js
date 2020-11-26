var form = $('#add-form')
form.submit(function(){
    $.ajax({
            url: form.attr('action'),
            type: 'get',
            success: function(response){
              alert(response);
            },
            error: function(rs, r){
              alert("Произошла ошибка");
            }
    });
    return false;
});