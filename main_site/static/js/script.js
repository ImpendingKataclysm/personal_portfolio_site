/* Language Options*/

$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip({
        placement: 'bottom',
        template:
            '<div class="tooltip language-tooltip" role="tooltip"><div class="arrow"></div><div class="tooltip-inner"></div></div>',
    });
});

/* Nav Menu */

const navBtn = document.querySelector('.navToggle')
const body = document.querySelector('body')

navBtn.addEventListener('click', (e) => {
    e.preventDefault();
    body.classList.toggle('navToggleActive');
})

/* Style Fixed Header on Scroll */

$(window).scroll(() => {
   if ($(this).scrollTop() > 10) {
       body.classList.add('fixedHeader');
   } else {
       body.classList.remove('fixedHeader');
   }
});

/* Home Page Sliders */

class MySlider {
    constructor(selector) {
        this.selector = selector;
        this.init();
    }

    init() {
        const swiperOptions = {
            slidesPerView: 1,
            spaceBetween: 10,
            navigation: {
                nextEl: `${this.selector} .swiper-button-next`,
                prevEl: `${this.selector} .swiper-button-prev`,
            },
            pagination: {
                el: `${this.selector} .swiper-pagination`,
                clickable: true,
            },
            breakpoints: {
                640: {
                    slidesPerView: 2,
                    spaceBetween: 16,
                },
                768: {
                    slidesPerView: 2,
                    spaceBetween: 16,
                },
                1024: {
                    slidesPerView: 2,
                    spaceBetween: 16,
                },
            },
        };

        this.swiper = new Swiper(this.selector, swiperOptions);
    }
}

const certificatesSlider = new MySlider('.certificatesSlider');
const portfolioSlider = new MySlider('.portfolioSlider');
