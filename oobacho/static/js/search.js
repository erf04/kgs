function find() {}

var input = document.getElementById("search");
var products = document.getElementsByClassName("product_name");
// console.log(products);
input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    var search = input.value;
    for (var i = 0; i < products.length; i++) {
      var product = products[i];
      if (product.innerHTML == search) {
        alert(product.innerHTML);
      }
    }
  }
});
