var pairTable = null;

$(document).ready(function () {
  $.ajaxSetup({
     headers:{
        'X-CSRFToken': csrftoken
     }
  });


  pairTable = $("#pair_table").DataTable({
    order: [[ 2, "desc" ]]
  });

  $("#submit").on("click", function () {
    console.log("Let's do this submit action");
    let entities = [];
    $('#pair_table input[type="checkbox"]:checked').each(function() {
      entities.push($(this).attr("data-entities"));
    });

    console.log({entities});
    $.post(suspiciousEntitiesURL, {
      entities
    });

    // const request = new Request(
    //     suspiciousEntitiesURL,
    //     {
    //       headers: {'X-CSRFToken': csrftoken},
    //       method: "POST",
    //       body: {"entities": JSON.stringify(entities)}
    //     }
    // );
    // console.log({request});
    // fetch(request, {
    //     method: 'POST',
    //     mode: 'same-origin'  // Do not send CSRF token to another domain.
    // }).then(function(response) {
    //     console.log("Got a response?")
    // });
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
