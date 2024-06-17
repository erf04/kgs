// $("#owl-demo").owlCarousel({
//   navigation: true,
// });
// $(window).on("load", () => {
//   $("body").addClass("loaded");
// });


// var email = document.getElementById("email");
// var email_div = document.getElementById("email-div");
// var placeholder = document.getElementById("placeholder");
// var height = email_div.clientHeight;
// var width = email_div.clientWidth;
// email.style.width = email_div.clientWidth;
// email.style.height = email_div.clientHeight;
// email.style.top = email_div.offsetHeight;
// email.style.paddingTop = $(email_div).css("padding-left");
// email.style.paddingTop += 30 + "px";
// console.log($(email_div).css("padding-top"));
// email.style.paddingLeft = $(email_div).css("padding-left");

// setInterval(() => {
//   if (email.value !== "") {
//     placeholder.innerHTML = "";
//   } else {
//     placeholder.innerHTML = "add email";
//   }
//   email_div.style.height = email_div.clientHeight;
//   email.style.width = email_div.clientWidth;
// }, 1);

// email.style.width = "500px";
// console.log(email.style.width);
// $('.owl-carousel').owlCarousel({
//   items: 3,
//   loop:true,
//   margin:10,
//   nav:true,
//   autoplay:true,
  // autoplayHoverPause:true,
  // autoplayTimeout:5000,
  // responsive:{
  //   0:{
  //     items:3
  //   },
  //   600:{
  //     items:3
  //   },
  //   1000:{
  //     items:3
  //   }
  // }
// })

// $(document).ready(function() {
  $("#owl-demo").owlCarousel({
    autoPlay: 3000,
    nav: true,
    items : 3,
    itemsDesktop : [1199,3],
    itemsDesktopSmall : [979,3]
  });
// });

function reveal() {
  var reveals = document.querySelectorAll(".reveal");

  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals[i].getBoundingClientRect().top;
    var elementVisible = 0;

    if (elementTop < windowHeight - elementVisible) {
      reveals[i].classList.add("active");
    } else {
      reveals[i].classList.remove("active");
    }
  }
}

window.addEventListener("scroll", reveal);
