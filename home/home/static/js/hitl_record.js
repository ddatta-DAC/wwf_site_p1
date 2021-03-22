var pairTable = null;

$(document).ready(function () {
  pairTable = $("#pair_table").DataTable({
    order: [[ 2, "desc" ]]
  });
});


window.onscroll = function() {myFunction()};
var navbar = document.getElementById("viznavbar");
var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}
