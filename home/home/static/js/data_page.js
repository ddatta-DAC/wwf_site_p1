var prettyName = {
  'score': 'Score',
  'shipmentmonth': 'Month Shipped',
  'consigneename': 'Consignee Name',
  'consigneecity': 'Consignee City',
  'consigneepanjivaid': 'Consignee',
  'consigneecountry': 'Consignee Country',
  'shipmentorigin': 'Shipment Origin',
  'province': 'Province',
  'countryofsale': 'Country of Sale',
  'transportmethod': 'Transport Method',
  'iscontainerized': 'Containerized',
  'valueofgoodsusd': 'Value',
  'hscode': 'HS Code',
  'hscodekeywords': 'HS Code Keywords',
  'adminregion': 'Admin Region',
  'tradetype': 'Trade Type'
}

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

$(document).ready(function () {
  // send ajax query to fill in table
  $.ajax({
    url: '/api/china_import', 
    method: 'GET',
    success: function (data) {
      buildTable(data);
    },
    error: function (error) {
      console.error(error);
    }
  });
});

function buildTable(data) {
  var columns = data.columns.map(function (title, i) {
    return {
      title: prettyName[title],
      data: i
    };
  });
  columns.unshift({
      "className":      'details-control',
      "orderable":      false,
      "data":           null,
      "defaultContent": ''
  });
  console.log(columns);

  var hiddenColumns = data.columns.map(function (title, i) {
    return {
      title,
      i
    };
  }).filter(function (d) {
    return data.main.indexOf(d.title) == -1;
  }).map(function (d) {
    return d.i + 1;
  });
  console.log(hiddenColumns);

  var table = $('#analysis_table').DataTable({
    columns: columns,
    columnDefs: [{
      targets: hiddenColumns,
      visible: false
    }],
    order: [[ 1, "desc" ]]
  });

  $('#analysis_table tbody').on('click', 'td.details-control', function () {
      var tr = $(this).closest('tr');
      var row = table.row( tr );
  
      if ( row.child.isShown() ) {
          // This row is already open - close it
          row.child.hide();
          tr.removeClass('shown');
      }
      else {
          // Open this row
          row.child( format(row.data()) ).show();
          tr.addClass('shown');
      }
  });

  table.rows.add(data.data).draw();
  
  function format(row) {
    console.log(row);
    return '<div class="expanded-row"><dl>' + row.reduce(function (prev, d, i) {
      if (hiddenColumns.indexOf(i + 1) != -1) {
        return prev + "<dt>" + prettyName[data.columns[i]] + "</dt><dd>" + d + "</dd>";
      }
      return prev;
    }, '') + '</dl><textarea></textarea></div>';
  }
}
