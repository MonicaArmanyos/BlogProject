/*$("#searchitem").autocomplete({
    source: "search.php",
    minLength: 3,
    select: function (event, ui) {
        window.location = "items.php?do=manage&itemid=" + ui.item.value;
    }
});
*/
$(".Subcribe").on('click',function() {
    $(this).toggleClass('Subcribe');
    if($(this).hasClass('Subcribe')){
        $(this).text('UnSubcribe');
    } else {
        $(this).text('Subcribe');
    }
});
