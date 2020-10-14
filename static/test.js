var queryUrl = "http://127.0.0.1:5001/";

// Perform a GET request to the query URL
d3.json(queryUrl, function(data) {
  // Once we get a response, send the data.features object to the createFeatures function
  console.log(data.ticket_id);
});
