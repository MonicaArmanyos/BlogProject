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






dislikestatus=$(".markdislike").text()
dislikecounters=$("#sdislike").text()
dislikecounters=parseInt(dislikecounters)
if(dislikestatus=="disliked")
{
$(".markdislike").text("dislike")
dislikecounters=dislikecounters-1
$("#sdislike").text(dislikecounters)

}









  $.ajax({
       url:"http://127.0.0.1:8000/blog/like/"+postid,
       success:function (response) {

       }




})


})



})