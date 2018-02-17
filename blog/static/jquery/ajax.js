$(document).ready(function()
{

$("#like").on("click",function(){
var postid=$(this).attr("data-post")
likestatus=$(".marklike").text()
likecounter=$("#slike").text()
likecounter=parseInt(likecounter)

if(likestatus=="like")
{
$(".marklike").text("liked")
likecounter=likecounter+1;

}
else
{
$(".marklike").text("like")
likecounter=likecounter-1;

}

$("#slike").text(likecounter)

  $.ajax({
       url:"http://127.0.0.1:8000/blog/like/"+postid,
       success:function (response) {

       }




})


})



})