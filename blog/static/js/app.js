$(document).ready(function(){
    $("#comment").on("submit",function(){
        var commText=$("#txt").val();
        var postId=this.getAttribute('data-post');
        var userId=this.getAttribute('data-user');
        $.ajax({
            url:'/blog/comment',
            data:{
                'comment':commText,
                'post':postId,
                'user':userId
            },

        });
    });
});