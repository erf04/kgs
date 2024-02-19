// $("#owl-demo").owlCarousel({
//   navigation: true,
// });
$(window).on("load", () => {
  $("body").addClass("loaded");
});

var owl = $(".owl-carousel");
owl.owlCarousel({
  nav: true,
  loop: true,
  margin: 10,
  autoplay: true,
  autoplayTimeout: 2000,
  autoplayHoverPause: true,
  responsiveClass: true,
  responsive: {
    0: {
      items: 1,
    },
    600: {
      items: 3,
    },
    1000: {
      items: 5,
    },
  },
});
