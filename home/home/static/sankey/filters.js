/**
* 0.  Initialize the left and right column dropdowns based on which of the files has been
*     selected.
* 1.  Initialize the left and right attribute dropdowns with a "SHOW ALL" option, and add event
*     listeners to those dropdowns for user selections
* 2.  Populate the left and right attribute dropdowns with the selection attributes provided in the
*     selected file, and add event listeners
* 3.  Populate the link flow option with the attributes provided in the selected file, set the
*     default value, and add an event listener
*/
function initializeDropdowns() {
	
	// 0
	var fileSelector = document.getElementById("optFile"); 
	var fileSelected = fileSelector.value;
	
	var leftColumn = document.getElementById("leftColumn");
	var rightColumn = document.getElementById("rightColumn");
	var element = document.createElement("option");
	
	if (fileSelected == "china_exp") {
		populateChinaExportDropdowns();
	} else if (fileSelected == "china_imp") {
		populateChinaImportDropdowns();		
	} else if (fileSelected == "peru_exp") {
		populatePeruExportDropdowns();
	} else if (fileSelected == "us_imp") {
		populateUSImportDropdowns();
	} //if-else
	
	// Add event listener
	fileSelector.onchange = function(d) {
		refreshLeftAndRightColumnDropdowns();
		newData();
		//redraw();
	};
	
	
	
	
	// 1
	addShowAllOption();
	
	
	
	
	// 2
	
	
	
	
	// 3
	
	// Make sure the Weight option is selected by default
	//var visOption = document.getElementById("visualizationFlowOption");
	//visOption.value = "WeightKg";

} //initializeDropdowns



function addShowAllOption() {

	var showAll = "SHOW ALL"; 
	
	// Initialize the left attribute dropdown
	var source = document.getElementById("leftAttribute"); 
	var el = document.createElement("option");
	el.textContent = showAll;
	el.value = showAll;
	source.appendChild(el);

	// Add event listener
	source.onchange = function(d) {
		redraw();
	};

	
	// Initialize the right attribute dropdown
	var dest = document.getElementById("rightAttribute"); 
	el = document.createElement("option");
	el.textContent = showAll;
	el.value = showAll;
	dest.appendChild(el);
	
	// Add event listener
	dest.onchange = function(d) {
		redraw();
	};

} //addShowAllOption



function refreshLeftAndRightColumnDropdowns() {
	var fileSelector = document.getElementById("optFile"); 
	var fileSelected = fileSelector.value;
	
	if (fileSelected == "china_exp") {
		populateChinaExportDropdowns();
	} else if (fileSelected == "china_imp") {
		populateChinaImportDropdowns();		
	} else if (fileSelected == "peru_exp") {
		populatePeruExportDropdowns();
	} else if (fileSelected == "us_imp") {
		populateUSImportDropdowns();
	} //if-else

} //refreshLeftAndRightColumnDropdowns



function removeOptions(selectbox) {
    var i;
    for(i = selectbox.options.length - 1 ; i >= 0 ; i--) {
        selectbox.remove(i);
    } //for
} //removeOptions



function populateChinaExportDropdowns() {
	var leftColumn = document.getElementById("leftColumn");
	var rightColumn = document.getElementById("rightColumn");
	var linkType = document.getElementById("visualizationFlowOption");
	var element = document.createElement("option");
	
	
	removeOptions(leftColumn);
	removeOptions(rightColumn);
	removeOptions(linkType);
	
	
	element = document.createElement("option");
	element.textContent = "Shipper Country";
	element.value = "ShipperCountry";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Shipper Country";
	element.value = "ShipperCountry";		
	rightColumn.appendChild(element);


	element = document.createElement("option");
	element.textContent = "Shipment Destination";
	element.value = "ShipmentDestination";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Shipment Destination";
	element.value = "ShipmentDestination";		
	rightColumn.appendChild(element);


	element = document.createElement("option");
	element.textContent = "Province";
	element.value = "Province";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Province";
	element.value = "Province";		
	rightColumn.appendChild(element);


	element = document.createElement("option");
	element.textContent = "Country of Sale";
	element.value = "CountryOfSale";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Country of Sale";
	element.value = "CountryOfSale";		
	rightColumn.appendChild(element);		


	element = document.createElement("option");
	element.textContent = "Transport Method";
	element.value = "TransportMethod";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Transport Method";
	element.value = "TransportMethod";		
	rightColumn.appendChild(element);
	
	
	element = document.createElement("option");
	element.textContent = "Value of Goods (USD)";
	element.value = "ValueOfGoodsUSD";		
	linkType.appendChild(element);
	

	leftColumn.value = "ShipperCountry";
	rightColumn.value = "ShipmentDestination";
	linkType.value = "ValueOfGoodsUSD";
	
} //populateChinaExportDropdowns



function populateChinaImportDropdowns() {
	var leftColumn = document.getElementById("leftColumn");
	var rightColumn = document.getElementById("rightColumn");
	var linkType = document.getElementById("visualizationFlowOption");
	var element = document.createElement("option");
	
	
	removeOptions(leftColumn);
	removeOptions(rightColumn);	
	removeOptions(linkType);
	
	
	element = document.createElement("option");
	element.textContent = "Consignee State Region";
	element.value = "ConsigneeStateRegion";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Consignee State Region";
	element.value = "ConsigneeStateRegion";		
	rightColumn.appendChild(element);


	element = document.createElement("option");
	element.textContent = "Consignee Country";
	element.value = "ConsigneeCountry";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Consignee Country";
	element.value = "ConsigneeCountry";		
	rightColumn.appendChild(element);


	element = document.createElement("option");
	element.textContent = "Shipment Origin";
	element.value = "ShipmentOrigin";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Shipment Origin";
	element.value = "ShipmentOrigin";		
	rightColumn.appendChild(element);


	element = document.createElement("option");
	element.textContent = "Province";
	element.value = "Province";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Province";
	element.value = "Province";		
	rightColumn.appendChild(element);		


	element = document.createElement("option");
	element.textContent = "Country of Sale";
	element.value = "CountryOfSale";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Country of Sale";
	element.value = "CountryOfSale";		
	rightColumn.appendChild(element);


	element = document.createElement("option");
	element.textContent = "Transport Method";
	element.value = "TransportMethod";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Transport Method";
	element.value = "TransportMethod";		
	rightColumn.appendChild(element);
	

	element = document.createElement("option");
	element.textContent = "Value of Goods (USD)";
	element.value = "ValueOfGoodsUSD";		
	linkType.appendChild(element);
	
	
	leftColumn.value = "ConsigneeStateRegion";
	rightColumn.value = "ConsigneeCountry";
	linkType.value = "ValueOfGoodsUSD";
	
} //populateChinaImportDropdowns



function populatePeruExportDropdowns() {
	var leftColumn = document.getElementById("leftColumn");
	var rightColumn = document.getElementById("rightColumn");
	var linkType = document.getElementById("visualizationFlowOption");
	var element = document.createElement("option");
	
	
	removeOptions(leftColumn);
	removeOptions(rightColumn);	
	removeOptions(linkType);
	
	
	element = document.createElement("option");
	element.textContent = "Shipper Country";
	element.value = "ShipperCountry";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Shipper Country";
	element.value = "ShipperCountry";		
	rightColumn.appendChild(element);


	element = document.createElement("option");
	element.textContent = "Shipment Destination";
	element.value = "ShipmentDestination";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Shipment Destination";
	element.value = "ShipmentDestination";		
	rightColumn.appendChild(element);


	element = document.createElement("option");
	element.textContent = "Port of Unlading";
	element.value = "PortOfUnlading";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Port of Unlading";
	element.value = "PortOfUnlading";		
	rightColumn.appendChild(element);


	element = document.createElement("option");
	element.textContent = "Transport Method";
	element.value = "TransportMethod";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Transport Method";
	element.value = "TransportMethod";		
	rightColumn.appendChild(element);		
	

	element = document.createElement("option");
	element.textContent = "Net Weight (kg)";
	element.value = "NetWeightKg";		
	linkType.appendChild(element);	
	
	element = document.createElement("option");
	element.textContent = "Value of Goods (FOBUSD)";
	element.value = "ValueOfGoodsFOBUSD";		
	linkType.appendChild(element);	


	leftColumn.value = "ShipperCountry";
	rightColumn.value = "ShipmentDestination";	
	linkType.value = "NetWeightKg";
	
} //populatePeruExportDropdowns



function populateUSImportDropdowns() {
	var leftColumn = document.getElementById("leftColumn");
	var rightColumn = document.getElementById("rightColumn");
	var linkType = document.getElementById("visualizationFlowOption");
	var element = document.createElement("option");
	
	removeOptions(leftColumn);
	removeOptions(rightColumn);	
	removeOptions(linkType);
	
	
	element = document.createElement("option");
	element.textContent = "Consignee Country";
	element.value = "ConsigneeCountry";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Consignee Country";
	element.value = "ConsigneeCountry";		
	rightColumn.appendChild(element);	
	
	
	element = document.createElement("option");
	element.textContent = "Shipper Country";
	element.value = "ShipperCountry";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Shipper Country";
	element.value = "ShipperCountry";		
	rightColumn.appendChild(element);	
	
	
	element = document.createElement("option");
	element.textContent = "Carrier";
	element.value = "Carrier";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Carrier";
	element.value = "Carrier";		
	rightColumn.appendChild(element);	
	
	
	element = document.createElement("option");
	element.textContent = "Shipment Origin";
	element.value = "ShipmentOrigin";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Shipment Origin";
	element.value = "ShipmentOrigin";		
	rightColumn.appendChild(element);	
	
	
	element = document.createElement("option");
	element.textContent = "Shipment Destination";
	element.value = "ShipmentDestination";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Shipment Destination";
	element.value = "ShipmentDestination";		
	rightColumn.appendChild(element);
	
	
	element = document.createElement("option");
	element.textContent = "Port of Unlading";
	element.value = "PortOfUnlading";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Port of Unlading";
	element.value = "PortOfUnlading";		
	rightColumn.appendChild(element);	
	
	
	element = document.createElement("option");
	element.textContent = "Port of Lading";
	element.value = "PortOfLading";
	leftColumn.appendChild(element);

	element = document.createElement("option");
	element.textContent = "Port of Lading";
	element.value = "PortOfLading";		
	rightColumn.appendChild(element);
	

	element = document.createElement("option");
	element.textContent = "Volume (TEU)";
	element.value = "VolumeTEU";		
	linkType.appendChild(element);	
	
	element = document.createElement("option");
	element.textContent = "Weight (KG)";
	element.value = "WeightKg";		
	linkType.appendChild(element);	
	
	
	leftColumn.value = "PortOfLading";
	rightColumn.value = "PortOfUnlading";
	linkType.value = "WeightKg";
	
} //populateUSImportDropdowns



/**
* Add listeners to the other controls (buttons, weight/value selection)
*/
function addListeners() {
	//var submitButton = document.getElementById("filterValueWeight");
	//submitButton.onclick = function(d) { filterValueAndOrWeight(); };
	
	//var resetButton = document.getElementById("resetFilters");
	//resetButton.onclick = function(d) { resetFilters(); };
	
	var visOption = document.getElementById("visualizationFlowOption");
	visOption.onchange = function(d) { changeLinkData(); };
	
	var leftColumn = document.getElementById("leftColumn");
	leftColumn.onchange = function(d) { updateNodesAndLinks(); };
	
	var rightColumn = document.getElementById("rightColumn");
	rightColumn.onchange = function(d) { updateNodesAndLinks(); };
	
} //addListener



function updateNodesAndLinks() {

	var leftAttr = document.getElementById("leftAttribute");
	var rightAttr = document.getElementById("rightAttribute");
	
	removeOptions(leftAttr);
	removeOptions(rightAttr);

	betterDataNodes = [];
	addShowAllOption();
	betterDataLinks = [];
	parseData(loadedData, true);
	redraw(); 	

} //updateNodesAndLinks



/**
* Add the provided country to the source dropdown
*
* @param country:  The country to add to the dropdown
*/
function addCountryToSource(country) {
	var source = document.getElementById("leftAttribute"); 
	var el = document.createElement("option");
	el.textContent = country.name;
	el.value = country.name;
	source.appendChild(el);
} //addCountryToSource


/**
* Add the provided country to the destination dropdown
*
* @param country:  The country to add to the dropdown
*/
function addCountryToDestination(country) {
	var dest = document.getElementById("rightAttribute"); 
	var el = document.createElement("option");
	el.textContent = country.name;
	el.value = country.name;
	dest.appendChild(el);
} //addCountryToDestination


/**
* Check the states of the source and destination dropdowns.  If necessary, filter
* the input dataset based on the user's selections
*
* @param d:  dataset of nodes that may or may not get filtered
*
* @return:  filtered (or unfiltered) dataset
*/
function applyFilters(d) {
	var source = document.getElementById("leftAttribute"); 
	var sourceFilter = source.value;
	
	var dest = document.getElementById("rightAttribute");
	var destFilter = dest.value;
	
	if (sourceFilter == "SHOW ALL" || destFilter == "SHOW ALL") {
		d = applySourceFilter(sourceFilter, d);
		d = applyDestinationFilter(destFilter, d);
	} else {
		d = applyBothFilters(sourceFilter, destFilter, d);
	} //if-else
	
	return d;
	
} // applyFilters


/**
* Given the source country filter state, filter (or don't) the dataset
*
* @param sourceFilter:  the value of the source country dropdown
* @param d:  dataset of nodes that may or may not get filtered
*
* @return:  filtered (or unfiltered) dataset
*/
function applySourceFilter(sourceFilter, d) {
	if (sourceFilter == "SHOW ALL") {
		return d;
	} else {
		return (d.name == sourceFilter) || (d.group == "right");
	} //if-else
} //applySourceFilter


/**
* Given the destination country filter state, filter (or don't) the dataset
*
* @param destFilter:  the value of the destination country dropdown
* @param d:  dataset of nodes that may or may not get filtered
*
* @return:  filtered (or unfiltered) dataset
*/
function applyDestinationFilter(destFilter, d) {
	if (destFilter == "SHOW ALL") {
		return d;
	} else {
		return (d.name == destFilter) || (d.group == "left");
	} //if-else
} //applyDestinationFilter


/**
* Given both source and destination country filter states, filter (or don't) the dataset
*
* @param sourceFilter:  the value of the source country dropdown
* @param destFilter:  the value of the destination country dropdown
* @param d:  dataset of nodes to filter
*
* @return:  filtered dataset
*/
function applyBothFilters(sourceFilter, destFilter, d) {
	return (d.name == sourceFilter) || (d.name == destFilter);
} //applyBothFilters


/**
* Check the states of the source and destination dropdowns.  If necessary, filter
* the input dataset based on the user's selections
*
* @param d:  dataset of links that may or may not get filtered
*
* @return:  filtered (or unfiltered) dataset
*/
function applyLinkFilter(d) {
	var source = document.getElementById("leftAttribute"); 
	var sourceFilter = source.value;
	
	var dest = document.getElementById("rightAttribute");
	var destFilter = dest.value;
		
	if (sourceFilter == "SHOW ALL" || destFilter == "SHOW ALL") {
		d = applyLinkSourceFilter(sourceFilter, d);
		d = applyLinkDestinationFilter(destFilter, d);
	} else {
		d = applyLinkBothFilters(sourceFilter, destFilter, d);
	} //if-else
	
	return d;
} //applyLinkFilter


/**
* Given the source country filter state, filter (or don't) the dataset
*
* @param sourceFilter:  the value of the source country dropdown
* @param d:  dataset of links that may or may not get filtered
*
* @return:  filtered (or unfiltered) dataset
*/
function applyLinkSourceFilter(sourceFilter, d) {
	if (sourceFilter == "SHOW ALL") {
		return d;
	} else {
		return (d.source.name == sourceFilter) && (d.target.group == "right");
	} //if-else
} //applyLinkSourceFilter


/**
* Given the destination country filter state, filter (or don't) the dataset
*
* @param destFilter:  the value of the destination country dropdown
* @param d:  dataset of links that may or may not get filtered
*
* @return:  filtered (or unfiltered) dataset
*/
function applyLinkDestinationFilter(destFilter, d) {
	if (destFilter == "SHOW ALL") {
		return d;
	} else {
		return (d.target.name == destFilter) && (d.source.group == "left");
	} //if-else
} //applyLinkDestinationFilter


/**
* Given both source and destination country filter states, filter (or don't) the dataset
*
* @param sourceFilter:  the value of the source country dropdown
* @param destFilter:  the value of the destination country dropdown
* @param d:  dataset of nodes to filter
*
* @return:  filtered dataset
*/
function applyLinkBothFilters(sourceFilter, destFilter, d) {
	return (d.source.name == sourceFilter) && (d.target.name == destFilter);
} //applyLinkBothFilters


/**
* If the user clicks on a country in the Sankey, update the dropdown state and filter
*
* @param group:  whether the user clicked on a source or a destination ("left" or "right")
* @param name:  the name of the source/destination on which the user clicked
*/
function nodeClickFilter(group, name) {
	
	var source = document.getElementById("leftAttribute"); 
	var dest = document.getElementById("rightAttribute");
	
	if (group == "left") {
		source.value = name;
	} else {
		dest.value = name;
	} //if-else
		
	redraw();
	
} //nodeClickFilter


/**
* If the user clicks on a link in the Sankey, update the dropdown states and filter
*
* @param sourceFilter:  the source country of the link
* @param destFilter:  the destination region of the link
*/
function linkClickFilter(sourceFilter, destFilter) {
	var source = document.getElementById("leftAttribute"); 
	source.value = sourceFilter;
	
	var dest = document.getElementById("rightAttribute");
	dest.value = destFilter;
	
	redraw();
} //linkClickFilter


/**
* If the user indicates an update to the value or weight filters (by clicking the update)
* button, check the textbox values, clear the Sankey links, and filter & redraw
*/
/*
function filterValueAndOrWeight() {
	
	var minV = document.getElementById("minValue"); 
	var maxV = document.getElementById("maxValue"); 
	var minW = document.getElementById("minWeight"); 
	var maxW = document.getElementById("maxWeight"); 
	
	minValue = minV.value.trim();
	maxValue = maxV.value.trim();
	minWeight = minW.value.trim();
	maxWeight = maxW.value.trim();
	
	if (minValue == "") {
		minValue = 0;
	} //if
	
	if (maxValue == "") {
		maxValue = 1481083;    //TODO: set this by searching for the max value in the dataset
	} //if
	
	if (minWeight == "") {
		minWeight = 0;
	} //if
	
	if (maxWeight == "") {
		maxWeight = 504004;    //TODO: set this by searching for the max weight in the dataset
	} //if

	//betterDataNodes = [];
	betterDataLinks = [];
	
	parseData(loadedData, false);
	redraw(); 
	
} //filterValueAndOrWeight
*/


/**
* If the user clicks the reset button, reset all controls (and the Sankey) to their default states
*/
function resetFilters() {
	var source = document.getElementById("leftAttribute"); 
	var dest = document.getElementById("rightAttribute");
	var visOption = document.getElementById("visualizationFlowOption");
/*
	var minV = document.getElementById("minValue"); 
	var maxV = document.getElementById("maxValue"); 
	var minW = document.getElementById("minWeight"); 
	var maxW = document.getElementById("maxWeight"); 
*/
	
	source.value = "SHOW ALL";
	dest.value = "SHOW ALL";
	visOption.value = "WeightKg";
	linkOption = "WeightKg";
/*
	minV.value = "";
	maxV.value = "";
	minW.value = "";
	maxW.value = "";
	
	minValue = 0;
	maxValue = 1481083;     //TODO:  don't hardcode
	minWeight = 0;
	maxWeight = 504004;     //TODO:  don't hardcode
*/	
	betterDataLinks = [];
	
	parseData(loadedData, false);
	redraw(); 
	
} //resetFilters


/**
* If the user switches between visualizing weight and value, update the Sankey
*/
function changeLinkData() {
	var visOption = document.getElementById("visualizationFlowOption");
	linkOption = visOption.value;
	betterDataLinks = [];
	parseData(loadedData, false);
	redraw(); 	
} //changeLinkData