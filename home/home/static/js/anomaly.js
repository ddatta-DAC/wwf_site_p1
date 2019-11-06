var mainTable = null;

$(document).ready(function () {
  buildTable({
    data: anomalyData,
    selector: '#anomaly_table',
    getData: {
      hide_compare: true,
    },
    datatablesSettings: {
      info: false,
      ordering: false,
      paging: false,
      searching: false,
    }
  });
  // buildTable(anomalyData, '#anomaly_table', true);

  // send ajax query to fill in table
  $.ajax({
    url: anomalyUrl, 
    method: 'GET',
    success: function (response) {
      // buildTable(data);
      mainTable = buildTable({
        data: response.data,
        getData: {
          hide: true
        },
        datatablesSettings: {
          createdRow: function ( row, data, index ) {
            response.style.forEach(function (pair) {
              console.log(data[pair.i], "==", pair.value);
              if (data[pair.i] == pair.value) {
                $('td', row).eq(pair.i + 1).addClass('highlight');
              }
            });
          }
        }
      })
    },
    error: function (error) {
      console.error(error);
    }
  });
});
