$(document).ready(function(){
    $('body').hide(0).delay(0).fadeIn(600);

    $(this).on('scroll', onScroll);
    $(window).on('resize', onScroll);
    $('.button-browse').on('click', onScroll);
});

var headerNode          = $('header');
var initialHeaderHeight = headerNode.height();

var MutationObserver    = window.MutationObserver || window.WebKitMutationObserver;
var myObserver          = new MutationObserver (mutationHandler);
var obsConfig           = { attributes: true };

headerNode.each (function () {
    myObserver.observe (this, obsConfig);
});

function mutationHandler(mutationRecords) {
    mutationRecords.forEach(function (mutation) {
        if (mutation.attributeName == 'class') {
            headerNode.on(
                'animationend webkitAnimationEnd oAnimationEnd MSAnimationEnd',
                function() {
                    if (headerNode.hasClass('slide-up')) {
                        headerNode.removeClass('smaller');
                    }

                    $('header.slide-up').removeClass('slide-up');

                }
            );
        }
    });
}


function onScroll(event){
    var currentScrollPos = $(document).scrollTop();

    var scrollY = window.pageYOffset || document.documentElement.scrollTop;
    var scrollDirection;
    scrollY <= this.lastScroll 
    ? scrollDirection = 'up'
    : scrollDirection = 'down';
    this.lastScroll = scrollY;

    if ((currentScrollPos >= initialHeaderHeight) && (scrollDirection == 'down')) {
        headerNode.addClass('smaller');
    };
    if ((currentScrollPos < (initialHeaderHeight + 100)) && (currentScrollPos >= initialHeaderHeight) && (scrollDirection == 'up')) {
        headerNode.addClass('slide-up');
    };
    if ((currentScrollPos < initialHeaderHeight) && (scrollDirection == 'up') && (headerNode.hasClass('smaller'))) {
        headerNode.addClass('slide-up');
    };

    console.log(currentScrollPos + ' >= ' + (initialHeaderHeight + 100) + ' /// ' + scrollDirection);
}