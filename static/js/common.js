$(function () {


});
// Screen size auto detect
function heightDetect() {
    $(".top_container").css("height", $(window).height());
};
heightDetect();
$(window).resize(function () {
    heightDetect();
});