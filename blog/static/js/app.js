$(document).ready(function(){
    $("#post").on("click",function(){
        var commText=$("#txt").val();
        var postId=this.getAttribute('data-post');
        var userId=this.getAttribute('data-user');
        $.ajax({
            url:"/blog/comment?comment="+commText+"&post="+postId+"&user="+userId,
            data:{

            },
            type:'GET',
            method:'GET',

        });
    });


     $(".reply").on("click",function(){
        var commentId=this.getAttribute('data-comment');
        var userId=this.getAttribute('data-user');
        var postId=this.getAttribute('data-post');
        var commText=$("#"+commentId).val();
        var username=this.getAttribute('username')
        alert(commText);
        $.ajax({
            url:"/blog/reply?comment="+commText+"&comId="+commentId+"&user="+userId,
            data:{

            },
            type:'GET',
            method:'GET',
            success:function()
            {
                location.href="http://127.0.0.1:8000/blog/post/"+postId



            },
            error:function()
            {
                location.href="http://127.0.0.1:8000/blog/post/"+postId
            }

        });
    });
});