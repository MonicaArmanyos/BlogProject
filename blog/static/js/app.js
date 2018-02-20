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
                $("#comments").append('<div><div>'+username+'</div><div>'+moment().format('MMM. D, YYYY, h:mm a')+'</div><div>'+commentJson.commentText+'</div><div id="replies'+commentJson.commentId+'"></div><textarea class="rep" id="'+commentJson.commentId+'" cols="30" rows="3" placeholder="Reply"></textarea><button class="reply" data-post="'+postId+'"  data-user="'+userId+'" data-comment="'+commentJson.commentId+'" type="submit" value="Post" username="'+username+'">Reply</button></div>')

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
                            $("#replies"+commentId).append('Reply from: <div>'+ username+'</div><div>'+moment().format('MMM. D, YYYY, h:mm a')+'</div><div>'+replyJson.replyText+'</div>')

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
                $("#replies"+commentId).append('Reply from: <div>'+ username+'</div><div>'+moment().format('MMM. D, YYYY, h:mm a')+'</div><div>'+replyJson.replyText+'</div>')

            }
        });
    });
});
