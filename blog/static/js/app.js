$(document).ready(function(){
    $("#post").on("click",function(){
        var commText=$("#txt").val();
        var postId=this.getAttribute('data-post');
        var userId=this.getAttribute('data-user');
        $.ajax({
            url:"http://127.0.0.1:8000/blog/comment?comment="+commText+"&post="+postId+"&user="+userId,
            data:{

            },
            type:'GET',
            method:'GET',

        });
    });
});