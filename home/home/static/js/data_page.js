var mainTable = null;
var primaryIndex = 0;

$(document).ready(function () {
  // send ajax query to fill in table
  $.ajax({
    url: tableUrl, 
    method: 'GET',
    success: function (data) {
      mainTable = buildTable({
        data
      });
    },
    error: function (error) {
      console.error(error);
    }
  });
});
