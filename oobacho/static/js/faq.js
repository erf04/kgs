$(window).on("load", function () {
    $("body").addClass("loaded");
  });
  document.querySelectorAll(".question").forEach(function (question) {
    question.addEventListener("click", function () {
      this.classList.toggle("open");
      var answer = this.querySelector(".answer");
    if (answer.style.maxHeight) {
      answer.style.maxHeight = null;
    } else {
      answer.style.maxHeight = answer.scrollHeight + "px";
    }
  });
});

topicLinks = document.getElementsByClassName("ids-links");
function border(n) {
  for (var i = 0; i < topicLinks.length; i++) {
    topicLinks[i].style.border = "0px"
  }
  topicLinks[n-1].style.borderLeft = "7px solid green";
}