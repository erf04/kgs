$("#owl-demo").owlCarousel({
  navigation: true,
});
$(window).on("load", () => {
  $("body").addClass("loaded");
});

// $(".owl-carousel").owlCarousel({
//   loop: true,
//   margin: 10,
//   nav: true,
//   responsive: {
//     0: {
//       items: 1,
//     },
//     600: {
//       items: 3,
//     },
//     1000: {
//       items: 5,
//     },
//   },
// });

var owl = $(".owl-carousel");
owl.owlCarousel({
  items: 4,
  loop: true,
  margin: 10,
  autoplay: true,
  autoplayTimeout: 3000,
  autoplayHoverPause: true,
});
$(".play").on("click", function () {
  owl.trigger("play.owl.autoplay", [1000]);
});
$(".stop").on("click", function () {
  owl.trigger("stop.owl.autoplay");
});
