/*$("#searchitem").autocomplete({
    source: "search.php",
    minLength: 3,
    select: function (event, ui) {
        window.location = "items.php?do=manage&itemid=" + ui.item.value;
    }
});
*/
$(".Subscribe").on('click',function() {
    cat_id = $(this).val();
    btn=this;

        $.ajax({

            url: '/blog/sub',
            data : {
                'catid':cat_id,
            },
            dataType:'json',
            success: function() {
                $(btn).text('Unsubscribe');
                console.log("ana subs")
                }
            })

   
      /*
    
        $.ajax({

            url: '/blog/unsub',
            data : {
                'catid':cat_id,
            },
            dataType:'json',
            success: function() {
            $(btn).text('Subscribe');
                console.log("ana msh subs")
                }
            })

   }   */  
     
});

