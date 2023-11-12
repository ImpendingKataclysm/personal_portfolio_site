/* Enable Tooltips */

const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
const tooltipTriggers = Array.from(tooltips);
const tooltipList = tooltipTriggers.map((tooltipTriggerEl) => (
    new bootstrap.Tooltip(tooltipTriggerEl)
));

/* Nav Menu */

const navBtn = document.querySelector('.navToggle')
const body = document.querySelector('body')

navBtn.addEventListener('click', () => (
   body.classList.toggle('navToggleActive')
));

/* Style Fixed Header on Scroll */

$(window).scroll(function() {
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
