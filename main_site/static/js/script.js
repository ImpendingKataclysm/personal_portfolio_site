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

/* Sliders */

const certificatesSlider = new Swiper(
    '.certificatesSlider',
    {
        slidesPerView: 1,
        spaceBetween: 10,
        navigation: {
            nextEl: `.swiper-button-next`,
            prevEl: `.swiper-button-prev`,
        },
        pagination: {
            el: `.swiper-pagination`,
            clickable: true,
        },
    }
);

const portfolioSlider = new Swiper(
    '.portfolioSlider',
    {
        slidesPerView: 1,
        spaceBetween: 10,
        navigation: {
            nextEl: `.swiper-button-next-main`,
            prevEl: `.swiper-button-prev-main`,
        },
        pagination: {
            el: `.swiper-pagination`,
            clickable: true,
        },
    }
);

const imageSlider = new Swiper(
    '.imageSlider',
    {
        slidesPerView: 1,
        spaceBetween: 5,
        navigation: {
            nextEl: `.swiper-button-next-img`,
            prevEl: `.swiper-button-prev-img`,
        },
        pagination: {
            el: `.swiper-pagination-img`,
            clickable: true,
        },
        nested: true,
    }
);
