
$('#options-form').submit(function (evt) {
  evt.preventDefault();
  console.log("Need to AJAX this thing");

  var attrs = [];
  var inputs = $('#options-form input:checked');
  inputs.each(function (input) {
    attrs.push(this.name);
  });

  $.ajax({
    url: '/viz_attr_selection', 
    method: 'GET',
    data: {
      attrs: attrs
    },
    success: function (data) {
      console.log(data);
    },
    error: function (error) {
      console.error(error);
    }
  });
});

var primaryIndex = 0;

$(document).ready(function () {
  // send ajax query to fill in table
  $.ajax({
    url: '/static/china_import.json', 
    method: 'GET',
    success: function (data) {
      buildTable(data);
    },
    error: function (error) {
      console.error(error);
    }
  });
});
