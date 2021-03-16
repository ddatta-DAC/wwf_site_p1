var pairTable = null;

$(document).ready(function () {
  pairTable = $("#pair_table").DataTable({
    order: [[ 2, "desc" ]]
  });
});
