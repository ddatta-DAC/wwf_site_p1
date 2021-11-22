var pairTable = null;

$(document).ready(function () {
  pairTable = $("#pair_table").DataTable({
    order: [[ 2, "desc" ]]
  });

  $("#submit").on("click", function () {
    console.log("Let's do this submit action");
    const entities = $('#pair_table input[type="checkbox"]:checked').map(function() {
      $(this).attr("data-entities")
    });

    console.log({entities});
    $.post(suspiciousEntitiesURL, {
      'entities[]': entities
    });
  })
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
