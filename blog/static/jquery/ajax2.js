$(document).ready(function()
{

$("#dislikepo").on("click",function(){
alert("ok")
var postid=$(this).attr("data-post")

  $.ajax({
       url:"http://127.0.0.1:8000/blog/dislike/"+postid,
       success:function (data) {
    alert(postid)
       }

})


})



})