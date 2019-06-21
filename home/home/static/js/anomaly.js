$(document).ready(function () {
  buildTable({
    data: anomalyData,
    selector: '#anomaly_table',
    hide: true,
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
      buildTable({
        data: data,
        hide: true
      })
    },
    error: function (error) {
      console.error(error);
    }
  });
});