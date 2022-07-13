/* Wengty Theme Scripts */

(function($){
    "use strict";
             
    $(window).on('load', function() {
        $('body').addClass('loaded');
    });

/*=========================================================================
	Sticky Header
=========================================================================*/
    function headerHeight(){
        var height = $("#header").height();
        $('.header-height').css('height', height+'px');
    }

    $(function() {
        var header = $("#header"),
            yOffset = 0,
            triggerPoint = 100;
        headerHeight();
        $(window).resize(headerHeight);
        $(window).on( 'scroll', function() {
            yOffset = $(window).scrollTop();

            if (yOffset >= triggerPoint) {
            	header.removeClass("animated cssanimation fadeIn");
                header.addClass("navbar-fixed-top  cssanimation animated fadeInTop");
            } else {
                header.removeClass("navbar-fixed-top cssanimation  animated fadeInTop");
                header.addClass("animated cssanimation fadeIn");
            }

        });
    });

/*=========================================================================
    Mobile Menu
=========================================================================*/  
    $(function(){
        $('#mainmenu').slicknav({
            prependTo: '.bottom-content-wrap',
            label: '',
            allowParentLinks: true
        });
    });

/*=========================================================================
    Sticky Footer
=========================================================================*/ 
    function stickyFooter(){
        var footerHeight = $('.sticky-footer').height(),
            bodySelector = $('body'),
            windowSize = $(window).width();
        if (windowSize >= 960) {
            bodySelector.css('margin-bottom', footerHeight+'px');
            $('.sticky-footer').removeClass('sticky-footer-disable');
        }else{
            bodySelector.css('margin-bottom', 0);
            $('.sticky-footer').addClass('sticky-footer-disable');
        }
    }
    stickyFooter();
    $(window).resize(stickyFooter);

/*=========================================================================
    Nivo slider 
=========================================================================*/
    $('#main-slider').nivoSlider({
        effect: 'random',
        animSpeed: 300,
        pauseTime: 5000,
        directionNav: true,
        manualAdvance: false,
        controlNavThumbs: false,
        pauseOnHover: true,
        controlNav: false,
        prevText: "<i class='ti-arrow-left'></i>",
        nextText: "<i class='ti-arrow-right'></i>"
    });
             
/*=========================================================================
	Counter Up Active
=========================================================================*/
	var counterSelector = $('.counter');
	counterSelector.counterUp({
		delay: 10,
		time: 1000
	});
             
/*=========================================================================
    Service Carousel
=========================================================================*/
    $('#service-carousel').owlCarousel({
        loop: true,
        margin: 25,
        autoplay: false,
        smartSpeed: 500,
        nav: true,
        navText: ['<i class="fa fa-caret-left"></i>', '<i class="fa fa-caret-right"></i>'],
        dots: false,
        responsive : {
            0 : {
                items: 1
            },
            480 : {
                items: 1,
            },
            768 : {
                items: 2,
            },
            992 : {
                items: 4,
            }
        }
    }); 

/*=========================================================================
    Project Carousel
=========================================================================*/
    $('#project-carousel').owlCarousel({
        loop: true,
        margin: 25,
        autoplay: false,
        smartSpeed: 500,
        nav: true,
        navText: ['<i class="fa fa-caret-left"></i>', '<i class="fa fa-caret-right"></i>'],
        dots: false,
        responsive : {
            0 : {
                items: 1
            },
            480 : {
                items: 1,
            },
            768 : {
                items: 2,
            },
            992 : {
                items: 4,
            }
        }
    });

/*=========================================================================
    Project Carousel
=========================================================================*/
    $('#project-img-carousel').owlCarousel({
        loop: true,
        margin: 25,
        autoplay: false,
        smartSpeed: 500,
        nav: true,
        navText: ['<i class="fa fa-caret-left"></i>', '<i class="fa fa-caret-right"></i>'],
        dots: false,
        responsive : {
            0 : {
                items: 1
            },
            480 : {
                items: 1,
            },
            768 : {
                items: 1,
            },
            992 : {
                items: 1,
            }
        }
    });

/*=========================================================================
    About Carousel
=========================================================================*/
    $('#about-carousel').owlCarousel({
        loop: true,
        margin: 25,
        autoplay: true,
        smartSpeed: 800,
        nav: true,
        navText: ['<i class="ti-arrow-left"></i>', '<i class="ti-arrow-right"></i>'],
        dots: false,
        responsive : {
            0 : {
                items: 1
            },
            480 : {
                items: 1,
            },
            768 : {
                items: 1,
            },
            992 : {
                items: 1,
            }
        }
    });

/*=========================================================================
    Isotope Active
=========================================================================*/
	$('.project-items').imagesLoaded( function() {

		 // Add isotope click function
		$('.project-filter li').on( 'click', function(){
	        $(".project-filter li").removeClass("active");
	        $(this).addClass("active");
	 
	        var selector = $(this).attr('data-filter');
	        $(".project-items").isotope({
	            filter: selector,
	            animationOptions: {
	                duration: 750,
	                easing: 'linear',
	                queue: false,
	            }
	        });
	        return false;
	    });

	    $(".project-items").isotope({
	        itemSelector: '.single-item',
	        layoutMode: 'masonry',
	    });
	});

/*=========================================================================
    Initialize smoothscroll plugin
=========================================================================*/
	smoothScroll.init({
		offset: 60
	});

/*=========================================================================
    Testimonial Carousel
=========================================================================*/
	$('#testimonial-carousel').owlCarousel({
        loop: true,
        margin: 15,
        autoplay: true,
        smartSpeed: 500,
        items: 1,
        nav: false,
        dots: true,
        responsive : {
			0 : {
				items: 1,
			},
			480 : {
				items: 1,
			},
			768 : {
				items: 2
			},
			992 : {
				items: 2
			}
		}
    });

/*=========================================================================
    Sponsor Carousel
=========================================================================*/
    $('#sponsor-carousel').owlCarousel({
        loop: true,
        margin: 40,
        autoplay: true,
        smartSpeed: 500,
        nav: false,
        dots: false,
        responsive : {
            0 : {
                items: 2
            },
            480 : {
                items: 3,
            },
            768 : {
                items: 4
            },
            992 : {
                items: 6
            }
        }
    });
		
/*=========================================================================
    Active venobox
=========================================================================*/
	$('.img-popup').venobox({
		numeratio: true,
		infinigall: true
	});

/*=========================================================================
    Active Nice Select
=========================================================================*/    
  $('select').niceSelect();

/*=========================================================================
    Vdeo Background
=========================================================================*/
    $(".video-bg").YTPlayer();

/*=========================================================================
	WOW Active
=========================================================================*/ 
    new WOW().init();             
             
/*=========================================================================
    Scroll To Top
=========================================================================*/     
    $(window).on( 'scroll', function () {
        if ($(this).scrollTop() > 100) {
            $('#scroll-to-top').fadeIn();
        } else {
            $('#scroll-to-top').fadeOut();
        }
    });
             
})(jQuery);





/* top scrolling txt */

var rightJS = {
    init: function(){
      rightJS.Tags = document.querySelectorAll('.rightJS');
      for(var i = 0; i < rightJS.Tags.length; i++){
        rightJS.Tags[i].style.overflow = 'hidden';
      }
      rightJS.Tags = document.querySelectorAll('.rightJS div');
      for(var i = 0; i < rightJS.Tags.length; i++){
        rightJS.Tags[i].style.position = 'relative';
        rightJS.Tags[i].style.right = '-'+rightJS.Tags[i].parentElement.offsetWidth+'px';
      }
      rightJS.loop();
    },
    loop: function(){
      for(var i = 0; i < rightJS.Tags.length; i++){
        var x = parseFloat(rightJS.Tags[i].style.right);
        x ++;
        var W = rightJS.Tags[i].parentElement.offsetWidth;
        var w = rightJS.Tags[i].offsetWidth;
        if((x/100) * W  > w) x = -W;
        if (rightJS.Tags[i].parentElement.parentElement.querySelector(':hover') !== rightJS.Tags[i].parentElement) rightJS.Tags[i].style.right = x + 'px';
      } 
      requestAnimationFrame(this.loop.bind(this));
    }
  };
  window.addEventListener('load',rightJS.init);
  
  /* JQUERY */
  
  $(function(){
    var rightJQ = {
      init: function(){
        $('.rightJQ').css({
          overflow: 'hidden'
        });
        $('.rightJQ').on('mouseover',function(){
          $('div', this).stop();
        });
        $('.rightJQ').on('mouseout',function(){
          $('div', this).animate({
            right: '100%'
          }, 16000, 'linear' );
        });
        rightJQ.loop();
      },
      loop: function(){
        $('.rightJQ div').css({
          position: 'relative',
          right: '-100%'
        }).animate({
          right: '100%'
        }, 16000, 'linear', rightJQ.loop);
      }
    };
    rightJQ.init();
  });
  

  /* slider */
