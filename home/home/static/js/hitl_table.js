var table;

function buildEpochTable(attrs) {
  var data = attrs.data;
  var tableId = '#main_table';
  if (attrs.selector) {
    tableId = attrs.selector;
  }

  if (!table) {
    var settings = {
      columns: data.columns,
      order: [[ 9, "desc" ]]
    };

    table = $(tableId).DataTable(settings);
  }

  table.rows.add(data.data).draw();
  
  return table;
}

function fetchEpoch(epoch) {
  $.ajax({
    url: `/api/epoch/${epoch}`, 
    method: 'GET',
    success: function (data) {
      console.log(data);
      // buildEpochTable(data);
      data.selector = "#main_table";
      table = buildTable(data);
    },
    error: function (error) {
      console.error(error);
    }
  });
}

$(document).ready(function () {
  fetchEpoch($("#epochs").val());

  $("#epochs").on("change", function () {
    if (table) {
      table.rows().remove().draw();
    }
    fetchEpoch(this.value);
  });

  $("#update-model").on("click", function () {
    $.ajax({
      url: "/models/update_model", 
      method: 'GET',
      success: function (data) {
        console.log(data);
        $.ajax({
          url: "/api/epoch/2016-01-01", 
          method: 'GET',
          success: function (data) {
            console.log(data);
            // buildEpochTable(data);
            // data.selector = "#main_table";
            // buildTable(data);
            table.rows().remove();
            table.rows.add(data.data).draw();
          },
          error: function (error) {
            console.error(error);
          }
        });

      },
      error: function (error) {
        console.error(error)
      }
    });
  });
});