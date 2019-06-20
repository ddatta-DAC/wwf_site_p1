$(document).ready(function () {
  buildTable(anomalyData, '#anomaly_table', true);

  // send ajax query to fill in table
  $.ajax({
    url: anomalyUrl, 
    method: 'GET',
    success: function (data) {
      buildTable(data);
    },
    error: function (error) {
      console.error(error);
    }
  });
});
