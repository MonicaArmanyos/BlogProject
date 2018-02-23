$(document).ready(function(){

    $("#post").on("click",function(){
        var commText=$("#txt").val();
        var postId=this.getAttribute('data-post');
        var userId=this.getAttribute('data-user');
        var username=this.getAttribute('username');
        $.ajax({
            url:"/blog/comment?comment="+commText+"&post="+postId+"&user="+userId,
            data:{

            },
            type:'GET',
            method:'GET',
            success:function(commentJson)
            {


                $("#txt").val("");
                $("#comments").append('<div class="text-center"  style=" background-color: rgba(0,0,0,0.3); width: 700px; margin-left: 230px">' +
                    '<div style="font-size:25px; color:white; font-weight: bold;">'+username+'</div>' +
                    '<div style="color: black; font-size: 12px;">'+moment().format('MMM. D, YYYY, h:mm a')+'</div>' +
                    '<br><div style="font-size:19px; color:#b8daff;font-weight: bold; ">'+commentJson.commentText+'</div><br></div>' +
                    '<div style="color:white; width: 500px; margin-left: 330px" id="replies'+commentJson.commentId+'">' +
                    '</div> <div class= "text-center" >' +
                    '<textarea class="rep" id="'+commentJson.commentId+'" cols="30" rows="3" placeholder="  Reply To Comment" style="border-radius: 20px;">' + '</textarea>' +
                    '<button style="border-radius: 10px;" class="reply" data-post="'+postId+'"  data-user="'+userId+'" data-comment="'+commentJson.commentId+'" type="submit" value="Post" username="'+username+'">Reply</button>' +
                    '</div>')

                $(".reply").on("click",function(){
                    var commentId=this.getAttribute('data-comment');
                    var userId=this.getAttribute('data-user');
                    var postId=this.getAttribute('data-post');
                    var commText=$("#"+commentId).val();
                    var username=this.getAttribute('username')
                    $.ajax({
                        url:"/blog/reply?comment="+commText+"&comId="+commentId+"&user="+userId,
                        data:{

                        },
                        type:'GET',
                        method:'GET',
                        success:function(replyJson)
                        {


                            $("#"+commentId).val("");
                            $("#replies"+commentId).append('   <div class="text-center"  style="color:black;background-color: rgba(0,0,0,0.1);"> <div style="font-size:18px; color:white; font-weight: bold;">'+ username+'</div><div style="color: black; font-size: 12px;">'+moment().format('MMM. D, YYYY, h:mm a')+'</div><br><div style="font-size:17px; color:#d58512;font-weight: bold; ">'+replyJson.replyText+'</div> <br></div>')

                        }
                    });
                });

            }

        });
    });


    $(".reply").on("click",function(){
        var commentId=this.getAttribute('data-comment');
        var userId=this.getAttribute('data-user');
        var postId=this.getAttribute('data-post');
        var commText=$("#"+commentId).val();
        var username=this.getAttribute('username')
        $.ajax({
            url:"/blog/reply?comment="+commText+"&comId="+commentId+"&user="+userId,
            data:{

            },
            type:'GET',
            method:'GET',
            success:function(replyJson)
            {


                $("#"+commentId).val("");
                $("#replies"+commentId).append('   <div class="text-center"  style="color:black;background-color: rgba(0,0,0,0.1);"> <div style="font-size:18px; color:white; font-weight: bold;">'+ username+'</div><div style="color: black; font-size: 12px;">'+moment().format('MMM. D, YYYY, h:mm a')+'</div><br><div style="font-size:17px; color:#d58512;font-weight: bold; ">'+replyJson.replyText+'</div> <br></div>')

            }
        });
    });

});
