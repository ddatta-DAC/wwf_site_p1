function buildEpochTable(attrs) {
  var data = attrs.data;
  var tableId = '#main_table';
  if (attrs.selector) {
    tableId = attrs.selector;
  }

  var settings = {
    columns: data.columns,
    order: [[ 9, "desc" ]]
  };

  var table = $(tableId).DataTable(settings);

  table.rows.add(data.data).draw();
  
  return table;
}

var mainTable;
$(document).ready(function () {
  console.log("Need to get table data for epoch", $("#epochs").val());
  $.ajax({
    url: `/api/epoch/${$("#epochs").val()}`, 
    method: 'GET',
    success: function (data) {
      console.log(data);
      mainTable = buildEpochTable(data);
    },
    error: function (error) {
      console.error(error);
    }
  });

});