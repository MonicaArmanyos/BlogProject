/*$("#searchitem").autocomplete({
    source: "search.php",
    minLength: 3,
    select: function (event, ui) {
        window.location = "items.php?do=manage&itemid=" + ui.item.value;
    }
});
*/
$(".Subcribe").on('click',function() {
    user_id =$(".Subcribe").request.user.id ;
    cat_id = $(".Subcribe").value();
    $(this).toggleClass('Subcribe');
    if($(this).hasClass('Subcribe')){
        $.ajax({

            url: "http://127.0.0.1:8000/blog/homepage/sub"+user_id+"/"+cat_id+"/" ,
            success: function() {
                console.log("ana subs")
                }
            })

        $(this).text('UnSubcribe');
    } else {
        $(this).text('Subcribe');
        $.ajax({

            url: "http://127.0.0.1:8000/blog/homepage/unsub"+user_id+"/"+cat_id+"/" ,
            success: function() {
                console.log("ana mesh sub");
            }
        })
    }
});
