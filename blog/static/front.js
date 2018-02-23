
$(".subs").on('click',function() {
    cat_id = $(this).val();
    btn=this;
    console.log($(btn).text())
    if($(btn).text()=='Subscribe') {
        $(btn).text('Unsubscribe');
        $.ajax({

            url: '/blog/sub',
            data: {
                'catid': cat_id,
            },
            dataType: 'json',
            success: function () {

            }
        })
    } else {
        $(btn).text('Subscribe');
        $.ajax({

            url: '/blog/unsub',
            data: {
                'catid': cat_id,
            },
            dataType: 'json',
            success: function () {

            }
        })
    }
});
