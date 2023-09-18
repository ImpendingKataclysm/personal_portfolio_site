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

/* Certificate Swiper*/
const swiper = new Swiper('.certificatesSlider', {
    slidesPerView: 1,
    spaceBetween: 10,
    pagination: {
        el: '.swiper-pagination',
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
});