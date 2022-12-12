const hamburgerMenu = document.querySelector('.hamburger');
const navigationBar = document.querySelector('.navigation');

hamburgerMenu.addEventListener('click', () => {
    navigationBar.classList.toggle('open-nav');
});