/* Style Fixed Header on Scroll */

window.addEventListener('scroll', () => {
    let fixedHeader = 'fixedHeader'
    if(window.scrollY > 10) {
        body.classList.add(fixedHeader);
    } else {
        body.classList.remove(fixedHeader);
    }
});

/* Enable Tooltips and Popovers */

const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
const tooltipTriggers = Array.from(tooltips);
const tooltipList = tooltipTriggers.map((tooltipTriggerEl) => (
    new bootstrap.Tooltip(tooltipTriggerEl)
));

const popovers = document.querySelectorAll('[data-bs-toggle="popover"]');
const popoverTriggers = Array.from(popovers);
const popoverList = popoverTriggers.map((popoverTriggerEl) => (
    new bootstrap.Popover(popoverTriggerEl)
));

/* Nav Menu */

const navBtn = document.querySelector('.navToggle');
const body = document.querySelector('body');

navBtn.addEventListener('click', () => (
   body.classList.toggle('navToggleActive')
));

/* Sliders */

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

/* LinkedIn Badge */

const linkedInLink = document.getElementById('linkedin-link');
const linkedInBadge = document.getElementById('linkedin-badge');

linkedInLink.addEventListener('mouseenter', () => {
    linkedInBadge.classList.toggle('show');
});

linkedInBadge.addEventListener('mouseenter', () => {
    linkedInBadge.classList.add('show');
});

linkedInBadge.addEventListener('mouseleave', () => {
    linkedInBadge.classList.remove('show');
})
