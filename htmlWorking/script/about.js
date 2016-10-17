//containers on the about page become a full page's height for optimal linking to by section
function resolveFullHeight() {
    $(".about-container").css("height", "auto");

    var h_window = $(window).height(),
        h_document = $(document).height(),
        fullHeight_top = $(".about-container").position().top,
        est_footerHeight = 112;

   // var h_fullHeight = (-1 * (est_footerHeight + (fullHeight_top - h_document)));

    //$(".about-container").height(h_fullHeight);
        $(".about-container").height(h_window);

}

resolveFullHeight();


var sections = $('container')
  , nav = $('nav')
  , nav_height = nav.outerHeight();
 
$(window).on('scroll', function () {
  var cur_pos = $(this).scrollTop();
 
  sections.each(function() {
    var top = $(this).offset().top - nav_height,
        bottom = top + $(this).outerHeight();
 
    if (cur_pos >= top && cur_pos <= bottom) {
      nav.find('a').removeClass('active');
      sections.removeClass('active');
 
      $(this).addClass('active');
      nav.find('a[href="about.html#'+$(this).attr('id')+'"]').addClass('active');
    }
  });
});


$(window).resize(function () {
    resolveFullHeight();
});