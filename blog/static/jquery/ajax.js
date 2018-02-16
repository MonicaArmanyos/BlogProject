$(document).ready(function()
{

$("#like").on("click",function(){
var postid=$(this).attr("data-post")

  $.ajax({
       url:"http://127.0.0.1:8000/blog/like/"+postid,
       success:function (data) {
    alert(postid)
       }




})






})


})