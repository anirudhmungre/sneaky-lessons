// Store our API endpoint as queryUrl.
var queryUrl = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2021-01-01&endtime=2021-01-02&maxlongitude=-69.52148437&minlongitude=-123.83789062&maxlatitude=48.74894534&minlatitude=25.16517337";


// Perform a GET request to the query URL.
d3.json(queryUrl).then(function (data) {
  console.log(data.features);
  // Using the features array sent back in the API data, create a GeoJSON layer, and add it to the map.

  // 1.
  // Pass the features to a createFeatures() function:
  createFeatures();

});

// 2. 
function createFeatures(earthquakeData) {

  // YOUR CODE GOES HERE
  // Save the earthquake data in a variable.

  // Pass the earthquake data to a createMap() function.
  createMap();

}


// 3.
// createMap() takes the earthquake data and incorporates it into the visualization:

function createMap(earthquakes) {
  // Create the base layers.
  var street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  })

  var topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
  });

  // Create a baseMaps object.
  var baseMaps = {
    "Street Map": street,
    "Topographic Map": topo
  };

  // Creat an overlays object.
  // YOUR CODE GOES HERE

  // Create a new map.
  // Edit the code to add the earthquake data to the layers.
  var myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 5,
    layers: [street]
  });

  // Create a layer control that contains our baseMaps.
  // Be sure to add an overlay Layer that contains the earthquake GeoJSON.
  L.control.layers(baseMaps, {
    collapsed: false
  }).addTo(myMap);

}
