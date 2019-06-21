// Empty initially; global variable to hold the raw data
var loadedData;
var betterDataNodes = [];
var betterDataLinks = [];

var linkOption = "WeightKg";

// var files = [
//   "sankey/data/panjiva_china_exports_01_2015_viz.csv",
//   "sankey/data/panjiva_china_imports_01_2015_viz.csv",
//   "sankey/data/panjiva_peru_exports_01_2015_viz.csv",
//   "sankey/data/panjiva_us_imports_01_2015_viz.csv"
// ];



$(document).ready(function () {
  // Load data asynchronously, then draw the Sankey
  d3.csv(files[0]).then(
    function(myData) { 
      loadedData = myData;
      initializeDropdowns();
      addListeners();
      parseData(loadedData, true);
      redraw(); 
    } //function
  ); //d3.csv
});

function newData() {

  // var fileSelector = document.getElementById("optFile"); 
  // var fileSelected = fileSelector.value;
  
  var useFile = 0;
  loadedData = null;
  betterDataNodes = [];
  addShowAllOption();
  betterDataLinks = [];
  
  if (fileSelected == "china_exp") {
    useFile = 0;
  } else if (fileSelected == "china_imp") {
    useFile = 1;
  } else if (fileSelected == "peru_exp") {
    useFile = 2;
  } else if (fileSelected == "us_imp") {
    useFile = 3;
  } //if-else

  d3.csv(files[0]).then(
    function(myData) { 
      loadedData = myData;
      //addListeners();
      parseData(loadedData, true);
      redraw(); 
    } //function
  ); //d3.csv
} //newData



/**
* Parse the input data to generate Sankey nodes and links
*
* @param myData:  data read from the CSV, pre-conversion into nodes and links
* @param resetDropdown:  whether or not to wipe the dropdowns and repopulate (currently not used)
*/
function parseData(myData, resetDropdowns) {
  var i;
  var count = 0;
  var node1;
  var node2;


  var leftColumn = document.getElementById("leftColumn");
  var rightColumn = document.getElementById("rightColumn");
  var linkType = document.getElementById("visualizationFlowOption");
  
  var leftAttr = leftColumn.value;
  var rightAttr = rightColumn.value;
  var flowOption = linkType.value;

  
  for (i = 1; i < myData.length; i++) {
    
    // Skip if the left and right are the same
    if (myData[i][leftAttr] == myData[i][rightAttr]) {
      continue;
    } //if
    
    
    
    // First node in the pair
    var nodeName = myData[i][leftAttr];
    /*
    if (nodeName == "") {
      //nodeName = "No Data (left)";
      continue;
    } //if
    */
    var tempNode = {
      "id": count,
      "name": nodeName,
      "group": "left"
    } 
    
    if (doesNodeAlreadyExist(nodeName) == -1) { 
      betterDataNodes.push(tempNode);
      if (resetDropdowns) {
        addCountryToSource(tempNode);
      } //if
      node1 = count;
      count++;
    } else {
      node1 = doesNodeAlreadyExist(nodeName);
    } //if-else
    
    
    
    
    // Second node in the pair
    nodeName = myData[i][rightAttr];
    /*
    if (nodeName == "") {
      //nodeName = "No Data (right)";
      continue;
    } //if    
    */
    tempNode = {
      "id": count,
      "name": nodeName,
      "group": "right"
    }

    if (doesNodeAlreadyExist(nodeName) == -1) { 
      betterDataNodes.push(tempNode);
      if (resetDropdowns) {
        addCountryToDestination(tempNode);
      } //if
      node2 = count;
      count++;
    } else {
      node2 = doesNodeAlreadyExist(nodeName);
    } //if-else
      
    
    // Link between them
    var linkValue = 0;
    linkValue = parseFloat(myData[i][flowOption]);
      
    if (isNaN(linkValue)) {
      //linkValue = 0;
      console.log('Yo, link value is NaN');
      continue;
    } //if
    
    
    tempLink = {
      "source": node1,
      "target": node2,
      "value": linkValue
    }
    
    if (!doesLinkAlreadyExist(tempLink)) {
      
//      var val = parseFloat(myData[i]["VolumeTEU"]);
//      var wgh = parseInt(myData[i]["WeightKg"]);
            
//      if ((val >= minValue) && (val <= maxValue) && (wgh >= minWeight) && (wgh <= maxWeight)) {
        betterDataLinks.push(tempLink);
//      } else {
        //console.log("Skipping shipment from " + node1.name + " to " + node2.name + " with quantity " + val + " and weight " + wgh + ".");
//      } //if
    } //if
    
  } //for 
  
} //parseData


/**
* Check to see if a node already exists, to prevent duplicates
*
* @param name:  name of the country/region to check
*
* @return:  node ID if the node exists, -1 if it doesn't
*/
function doesNodeAlreadyExist(name) {
  var i;
  for (i = 0; i < betterDataNodes.length; i++) {
    if (betterDataNodes[i].name == name) {
      return betterDataNodes[i].id;
    } //if
  } //for
  return -1;
} //doesNodeAlreadyExist


/**
* Check to see if a link already exists, to prevent duplicates.  If it does already exist, add the 
* value of the input link to the current total
*
* @param name:  object containing link properties to check
*
* @return:  true if the link already existed, false if it didn't
*/
function doesLinkAlreadyExist(link) {
  if (link.value == 0) {
    return true;
  } //if
  
  var i;
  for (i = 0; i < betterDataLinks.length; i++) {
    if (betterDataLinks[i].source == link.source && betterDataLinks[i].target == link.target) {
      betterDataLinks[i].value += link.value;
      return true;
    } //if
  } //for
  return false;
} //doesLinkAlreadyExist