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
    success: function (data) {
      // buildTable(data);
      mainTable = buildTable({
        data: data,
        getData: {
          hide: true
        }
      })
    },
    error: function (error) {
      console.error(error);
    }
  });
});
