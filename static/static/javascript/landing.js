(function() {
    $('.bounce > a').on('click', function() {
        $('html, body').animate({
           scrollTop: $('#quote').offset().top 
        }, 1000);
        return false;
    });
    
    $('.news-post').mouseenter(function() {
        $(this).find('.news-overlay').addClass('is-hovered');
    });
    
    $('.news-post').mouseleave(function() {
        $(this).find('.news-overlay').removeClass('is-hovered');
    });
})();