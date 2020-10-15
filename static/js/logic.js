// Creating map object
var myMap = L.map("map", {
    center: [39.1653, -86.5264],
    zoom: 20
  });
  
  // Adding tile layer
  L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
  }).addTo(myMap);
  
  // Use this link to get the geojson data.
  var link = "/";
  
  // Grabbing our GeoJSON data..
  // 17.2 Activity 3 to add cluster group
  d3.json(link, function(data) {
    console.log(data)
    var potholes = data.location
    for (var i = 0; i < potholes.length; i++) {
        var pothole = potholes[i];
        L.marker([pothole[12], pothole[13]])
            // pop up not working...
            .bindPopup("<h1>" + pothole[8]+ "</h1>")
            .addTo(myMap);
    }
});