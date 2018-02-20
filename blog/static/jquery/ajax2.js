$(document).ready(function()
{

    $("#dislikepo").on("click",function(){
        var postid=$(this).attr("data-post")
        likestatus=$(".markdislike").text()
        dislikecounter=$("#sdislike").text()
        dislikecounter=parseInt(dislikecounter)
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



        likecounters=$("#slike").text()
        liketatus=$(".marklike").text()
        likecounters=parseInt(likecounters)


        if(liketatus=="liked")
        {
            $(".marklike").text("like")
            likecounters=likecounters-1
            $("#slike").text(likecounters)

        }





        $.ajax({
            url:"http://127.0.0.1:8000/blog/dislike/"+postid,
            success:function (data) {

                if (data.del==1)
                {
                    $("#exampleModal").modal("show")


                }


            }




        })

    })

})