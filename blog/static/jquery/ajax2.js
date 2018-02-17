$(document).ready(function()
{

$("#dislikepo").on("click",function(){
var postid=$(this).attr("data-post")
likestatus=$(".markdislike").text()
dislikecounter=$("#sdislike").text()
dislikecounter=parseInt(dislikecounter)
console.log(dislikecounter)
if(likestatus=="dislike")
{
$(".markdislike").text("disliked")
dislikecounter=dislikecounter+1;

}
else
{
$(".markdislike").text("dislike")
dislikecounter=dislikecounter-1;
}

$("#sdislike").text(dislikecounter)

  $.ajax({
       url:"http://127.0.0.1:8000/blog/dislike/"+postid,
       success:function (data) {
    alert(postid)
       }

})


})



})