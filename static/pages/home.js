$(function(){
    $(".section_link li")
        .mouseenter(function () {
           var description = $(".description", this).html();
           var title = $("a", this).html();
            var container = $(".description_container");
           $(".title", container).html(title);
           $(".body", container).html(description);
            container.fadeIn()
        })
        .mouseleave(function() {
            $(".description_container").fadeOut();
        });
});
