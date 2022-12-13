const swiper1 = new Swiper('#swiper1', {
  direction: 'horizontal',
  loop: true,
  pagination: {
    el: '.swiper-pagination',
  },
  autoplay: {
    delay: 3000
  }
});