
function buildTable(data, tableId = '#analysis_table') {
  var primaryIndex = data.id_index;

  var table = $(tableId).DataTable({
    columns: data.columns,
    columnDefs: [{
      targets: data.hidden_cols,
      visible: false
    }],
    order: [[ 1, "desc" ]]
  });

  $(tableId + ' tbody').on('click', 'td.details-control', function () {
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
  
  function getComment(pid) {
    if (pid in data.comment_data) {
      return data.comment_data[pid];
    }
    return '';
  }

  function format (row) {
      var div = $('<div/>')
          .addClass('loading')
          .text('Loading...');
   
      $.ajax({
          url: expandRowUrl + '/' + row[primaryIndex],
          data: {
            hide: true,
          },
          dataType: 'json',
          success: function (json) {
              div
                  .html(json.html)
                  .removeClass('loading');
          }
      });
      return div;
  }
}

function setThumbs(panjivarecordid) {
  var value = $('#thumbs-' + panjivarecordid + ' input:checked').val()
  console.log("Need to set value of", panjivarecordid, "to", value);
  $('#thumbs-spin-' + panjivarecordid).removeClass('hidden');
  $('#thumbs-check-' + panjivarecordid).addClass('hidden')
  $('#thumbs-error-' + panjivarecordid).addClass('hidden')

  $.ajax({
    url: thumbsUrl, 
    method: 'POST',
    data: {
      panjivarecordid,
      value,
      csrfmiddlewaretoken: csrfToken,
    },
    success: function (data) {
      console.log(data);
      var rowIndexes = [];
      table.rows( function (idx, row, node) {
        if(row[primaryIndex] == panjivarecordid){
          rowIndexes.push(idx);                  
        }
        return false;
      });

      if (rowIndexes.length > 0) {
        table.cell(rowIndexes[0], primaryIndex+3).data(data.thumbs)
      } else {
        console.error('Cannot find row with id', panjivarecordid);
      }

      $('#thumbs-spin-' + panjivarecordid).addClass('hidden');
      $('#thumbs-check-' + panjivarecordid).removeClass('hidden');
    },
    error: function (error) {
      console.error(error);
      $('#thumbs-spin-' + panjivarecordid).addClass('hidden');
      $('#thumbs-error-' + panjivarecordid).removeClass('hidden');
    }
  });
}

function submitComment(panjivarecordid) {
  console.log(panjivarecordid);
  $('#spin-' + panjivarecordid).removeClass('hidden');
  $('#check-' + panjivarecordid).addClass('hidden')
  $('#error-' + panjivarecordid).addClass('hidden')

  $.ajax({
    url: commentUrl, 
    method: 'POST',
    data: {
      panjivarecordid,
      comment: $('#comments-text-area-' + panjivarecordid).val(),
      csrfmiddlewaretoken: csrfToken,
    },
    success: function (data) {
      console.log(data);

      var rowIndexes = [];
      table.rows( function (idx, row, node) {
        if(row[primaryIndex] == panjivarecordid){
          rowIndexes.push(idx);                  
        }
        return false;
      });

      if (rowIndexes.length > 0) {
        table.cell(rowIndexes[0], primaryIndex+2).data(data.comment)
      } else {
        console.error('Cannot find row with id', panjivarecordid);
      }

      $('#spin-' + panjivarecordid).addClass('hidden');
      $('#check-' + panjivarecordid).removeClass('hidden');
    },
    error: function (error) {
      console.error(error);
      $('#spin-' + panjivarecordid).addClass('hidden');
      $('#error-' + panjivarecordid).removeClass('hidden');
    }
  });

}
