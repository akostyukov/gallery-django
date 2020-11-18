$('.btn').click(function(){
    $.ajax({
            url: "like/1/",
            type: 'get',
            success: function(response){
              alert("Все четко");
            },
            error: function(rs, r){
              alert("Ты обосрался");
            }
  })
 });