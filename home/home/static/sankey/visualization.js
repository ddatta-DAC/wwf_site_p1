// Grab the chart div from the HTML page; retrieve its width and height
var chartDiv = document.getElementById("chart");
var section = document.getElementById("svg-section");
var width = chartDiv.clientWidth;
var height = 3000;

// Number formatting
var formatNumber = d3.format(",.0f"),
  format = function(d) { 
    var linkType = document.getElementById("visualizationFlowOption");
    var linkOption = linkType.value;
    
    if (linkOption == "WeightKg" || linkOption == "NetWeightKg") {
      return formatNumber(d) + " KG"; 
    } else if (linkOption == "ValueOfGoodsFOBUSD" || linkOption == "ValueOfGoodsUSD") {
      return "$" + formatNumber(d);
    } else if (linkOption == "VolumeTEU") {
      return formatNumber(d) + " (TEU)";
    } else {
      return formatNumber(d);
    } //if-else
  },
  color = d3.scaleOrdinal(d3.schemeCategory10);

// Create the SVG "canvas"  
var svg = d3.select("#chart")
  .append("svg");

// Setting up the variables for the Sankey diagram  
var sankey = d3.sankey();
var path = sankey.link();


/**
* The function that actually draws the Sankey
*/
function redraw() {
  
  // Wipe everything currently in the SVG
  svg.selectAll("*").remove();
  
  // Get the new width and height of the chart div
  width = chartDiv.clientWidth;
  height = chartDiv.clientHeight;
  
  // Reset the width and height of the SVG 
  svg.attr("width", width)
     .attr("height", height);
     
     
  // Set basic Sankey properties, including the size    
  // TODO: we shouldn't reset the positions of the nodes and links on this resize redraw
  sankey.nodeWidth(15)
      .nodePadding(5)
      .size([width, height]);   
      
  // Add the nodes and links to the Sankey  
  sankey.nodes(betterDataNodes)
      .links(betterDataLinks)
      .layout(32);

  // Data binding and properties for the links in the Sankey  
  var link = svg.append("g").selectAll(".link")
    .data(betterDataLinks)
    .enter()
    .filter( function(d) { return applyLinkFilter(d); })
      .append("path")
      .attr("class", "link")
      .attr("d", path)
      .style("stroke-width", function(d) { return Math.max(1, d.dy); })
      .sort(function(a, b) { return b.dy - a.dy; })
      .on("click", function(d) { linkClickFilter(d.source.name, d.target.name); });

  // Add a tooltip onto the links
  link.append("title")
    .text(function(d) { return d.source.name + " → " + d.target.name + "\n" + format(d.value); });

  // Data binding and properties for the nodes in the Sankey
  var node = svg.append("g").selectAll(".node")
    .data(betterDataNodes)
    .enter()
    .filter( function(d) { return applyFilters(d); })
        .append("g")
      .attr("class", "node")
      .attr("transform", function(d) {
        return "translate(" + d.x + "," + d.y + ")";
      })
    .call(d3.drag()
      .subject(function(d) { return d; })
      .on("start", function() { this.parentNode.appendChild(this); })
      .on("drag", dragmove));

  node.append("rect")
    .attr("height", function(d) { return d.dy; })
    .attr("width", sankey.nodeWidth())
    .style("fill", function(d) { return d.color = color(d.name.replace(/ .*/, "")); })
    .style("stroke", function(d) { return d3.rgb(d.color).darker(2); })
    .on("click", function(d) { nodeClickFilter(d.group, d.name); } )
    .append("title")
      .text(function(d) { return d.name + "\n" + format(d.value); });

  node.append("text")
    .attr("x", -6)
    .attr("y", function(d) { return d.dy / 2; })
    .attr("dy", ".35em")
    .attr("text-anchor", "end")
    .attr("transform", null)
    .text(function(d) { return d.name; })
    .filter(function(d) { return d.x < width / 2; })
      .attr("x", 6 + sankey.nodeWidth())
      .attr("text-anchor", "start");

  // If the analyst drags on a node, relayout the Sankey based on the drag
  function dragmove(d) {
    d3.select(this).attr("transform", "translate(" + d.x + "," + (d.y = Math.max(0, Math.min(height - d.dy, d3.event.y))) + ")");
    sankey.relayout();
    link.attr("d", path);
  } //dragMove
  
} //redraw


// Add event listener on window for resize responsiveness
window.addEventListener("resize", function() { redraw(loadedData); })