var overlay = document.getElementById("overlay");
function showImage(img) {
  img.classList.add("showedImg");
  img.firstElementChild.setAttribute("controls", "");
  overlay.appendChild(img);
  overlay.classList.add("blackBack");
}
