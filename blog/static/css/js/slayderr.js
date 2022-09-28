var swiper = new Swiper('.blog-slider', {
    effect: 'fade',
    loop: true,
    mousewheel: {
        invert: false,
    },
    autoHeight: true,
    pagination: {
        el: '.blog-slider__pagination',
        clickable: true,
    }
    
});

