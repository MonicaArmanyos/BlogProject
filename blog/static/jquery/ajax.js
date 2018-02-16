$(document).ready(function()
{

$("#like").on("click",function(){


  $.ajax({
       url:"http://127.0.0.1:8000/blog/like",

       success:function (data) {
    alert("any")
       }




})






})


})