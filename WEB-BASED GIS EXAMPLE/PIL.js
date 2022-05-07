// This javascript creates a map with multiple markers throughout Leeds, where each marker represents a property for sale 
var map; 

//These set the maps starting coordinates and zoom.
var myCentreLat = 53.825;
var myCentreLng = -1.51;
var initialZoom = 11;
var activeWindow;


function infoCallback(infowindow, marker) { 
    return function() {
        //Closes the active infowindow and opens a new infowindow
        if (activeWindow != null) {
            activeWindow.close();
        }
        infowindow.open(map,marker); 
        //Store new window in the global infowindow variable
        activeWindow = infowindow; 
    };
}

//This function adds the markers to the map display and sets the markers inital parameters, as well as the infowindow for each marker. The marker is then styled, so it shows the house icon 
function addMarker(myPos,myTitle,myInfo) {
	marker = new google.maps.Marker({
	position: myPos,
	map: map,
	title: myTitle,
	icon: 'http://chart.apis.google.com/chart?chst=d_map_pin_icon&chld=home|EA6666',
	animation: google.maps.Animation.DROP,
	});
   
    var infowindow = new google.maps.InfoWindow({content: myInfo});
   
   google.maps.event.addListener(marker,'click', infoCallback(infowindow, marker));
}	
		
//For when the reset button is clicked, it runs this function which resets the map to its starting position and zoom, whilst clearing the map of any markers
function initialize() {
  var latlng = new google.maps.LatLng(myCentreLat,myCentreLng);
  var myOptions = {
    zoom: initialZoom,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  map = new google.maps.Map(document.getElementById("map_canvas"),myOptions);
 
 //Adds polygon boundary around Leeds, sourcing the lat lng data stored in Leedsboundarycoords.js
 var leedsboundary = LeedsBoundaryCoords;
	var boundary = new google.maps.Polygon({
    path: leedsboundary,
    geodesic: true,
	strokeColor: "#E35C5C",
    strokeOpacity: 1,
    strokeWeight: 2,
	fillOpacity: 0,
	});
   boundary.setMap(map);
 
 }

// This function and all the functions underneath plots different markers which correspond with different variables in the os_marker data. These include different price ranges for each property. Adding a multilayered 
// function would provide a lot more functionality however, the coding becomes more complex, so this is an idea for the future. For instance, if the reader wants to know all properties within a price range that is also
// a particular type of house or has X amount of bedrooms. 
function plot0100K() {
 for (var i = 0; i < os_markers.length; i++)	{ 
    if (os_markers[i].no == '1')	{	
    var info = "<div class=infowindow><h1>£" + os_markers[i].price + "</h1><h3>" + os_markers[i].address  + 
	  "</h3><ul><li><i class='fa fa-fw fa-bed'></i>  " + os_markers[i].bedrooms +
	  "</li><li><i class='fa fa-fw fa-bath'></i>  " + os_markers[i].baths +
	  "</li><li><i class='fas fa-couch'></i>  " + os_markers[i].reception +
	  "</li></ul><h4><em> Address: " + os_markers[i].address + "</h4></em><h5><a href='" + os_markers[i].links + "'>Click here for more information</a></div>";
	  
	  var osPt = new OSRef(os_markers[i].easting,os_markers[i].northing);
      var llPt = osPt.toLatLng(osPt);
      llPt.OSGB36ToWGS84();
	  
	  addMarker(new google.maps.LatLng(llPt.lat,llPt.lng),os_markers[i].price,info)	;
	
	  
	  
	}
 }
}

function plot100150K() {
 for (var i = 0; i < os_markers.length; i++)	{ 
    if (os_markers[i].no == '2')	{	
    var info = "<div class=infowindow><h1>£" + os_markers[i].price + "</h1><h3>" + os_markers[i].address  + 
	  "</h3><ul><li><i class='fa fa-fw fa-bed'></i>  " + os_markers[i].bedrooms +
	  "</li><li><i class='fa fa-fw fa-bath'></i>  " + os_markers[i].baths +
	  "</li><li><i class='fas fa-couch'></i>  " + os_markers[i].reception +
	  "</li></ul><h4><em> Address: " + os_markers[i].address + "</h4></em><h5><a href='" + os_markers[i].links + "'>Click here for more information</a></div>";
	  
	  var osPt = new OSRef(os_markers[i].easting,os_markers[i].northing);
      var llPt = osPt.toLatLng(osPt);
      llPt.OSGB36ToWGS84();
	  
	  addMarker(new google.maps.LatLng(llPt.lat,llPt.lng),os_markers[i].price,info)	;
	}
 }
}

function plot150200K() {
 for (var i = 0; i < os_markers.length; i++)	{ 
    if (os_markers[i].no == '3')	{	
    var info = "<div class=infowindow><h1>£" + os_markers[i].price + "</h1><h3>" + os_markers[i].address  + 
	  "</h3><ul><li><i class='fa fa-fw fa-bed'></i>  " + os_markers[i].bedrooms +
	  "</li><li><i class='fa fa-fw fa-bath'></i>  " + os_markers[i].baths +
	  "</li><li><i class='fas fa-couch'></i>  " + os_markers[i].reception +
	  "</li></ul><h4><em> Address: " + os_markers[i].address + "</h4></em><h5><a href='" + os_markers[i].links + "'>Click here for more information</a></div>";
	  
	  var osPt = new OSRef(os_markers[i].easting,os_markers[i].northing);
      var llPt = osPt.toLatLng(osPt);
      llPt.OSGB36ToWGS84();
	  
	  addMarker(new google.maps.LatLng(llPt.lat,llPt.lng),os_markers[i].price,info)	;
	}
 }
}

function plot200250K() {
 for (var i = 0; i < os_markers.length; i++)	{ 
    if (os_markers[i].no == '4')	{	
    var info = "<div class=infowindow><h1>£" + os_markers[i].price + "</h1><h3>" + os_markers[i].address  + 
	  "</h3><ul><li><i class='fa fa-fw fa-bed'></i>  " + os_markers[i].bedrooms +
	  "</li><li><i class='fa fa-fw fa-bath'></i>  " + os_markers[i].baths +
	  "</li><li><i class='fas fa-couch'></i>  " + os_markers[i].reception +
	  "</li></ul><h4><em> Address: " + os_markers[i].address + "</h4></em><h5><a href='" + os_markers[i].links + "'>Click here for more information</a></div>";
	  
	  var osPt = new OSRef(os_markers[i].easting,os_markers[i].northing);
      var llPt = osPt.toLatLng(osPt);
      llPt.OSGB36ToWGS84();
	  
	  addMarker(new google.maps.LatLng(llPt.lat,llPt.lng),os_markers[i].price,info)	;
	}
 }
}

function plot250300K() {
 for (var i = 0; i < os_markers.length; i++)	{ 
    if (os_markers[i].no == '5')	{	
    var info = "<div class=infowindow><h1>£" + os_markers[i].price + "</h1><h3>" + os_markers[i].address  + 
	  "</h3><ul><li><i class='fa fa-fw fa-bed'></i>  " + os_markers[i].bedrooms +
	  "</li><li><i class='fa fa-fw fa-bath'></i>  " + os_markers[i].baths +
	  "</li><li><i class='fas fa-couch'></i>  " + os_markers[i].reception +
	  "</li></ul><h4><em> Address: " + os_markers[i].address + "</h4></em><h5><a href='" + os_markers[i].links + "'>Click here for more information</a></div>";
	  
	  var osPt = new OSRef(os_markers[i].easting,os_markers[i].northing);
      var llPt = osPt.toLatLng(osPt);
      llPt.OSGB36ToWGS84();
	  
	  addMarker(new google.maps.LatLng(llPt.lat,llPt.lng),os_markers[i].price,info)	;
	}
 }
}

function plot300350K() {
 for (var i = 0; i < os_markers.length; i++)	{ 
    if (os_markers[i].no == '6')	{	
    var info = "<div class=infowindow><h1>£" + os_markers[i].price + "</h1><h3>" + os_markers[i].address  + 
	  "</h3><ul><li><i class='fa fa-fw fa-bed'></i>  " + os_markers[i].bedrooms +
	  "</li><li><i class='fa fa-fw fa-bath'></i>  " + os_markers[i].baths +
	  "</li><li><i class='fas fa-couch'></i>  " + os_markers[i].reception +
	  "</li></ul><h4><em> Address: " + os_markers[i].address + "</h4></em><h5><a href='" + os_markers[i].links + "'>Click here for more information</a></div>";
	  
	  var osPt = new OSRef(os_markers[i].easting,os_markers[i].northing);
      var llPt = osPt.toLatLng(osPt);
      llPt.OSGB36ToWGS84();
	  
	  addMarker(new google.maps.LatLng(llPt.lat,llPt.lng),os_markers[i].price,info)	;
	}
 }
}

function plot350400K() {
 for (var i = 0; i < os_markers.length; i++)	{ 
    if (os_markers[i].no == '7')	{	
    var info = "<div class=infowindow><h1>£" + os_markers[i].price + "</h1><h3>" + os_markers[i].address  + 
	  "</h3><ul><li><i class='fa fa-fw fa-bed'></i>  " + os_markers[i].bedrooms +
	  "</li><li><i class='fa fa-fw fa-bath'></i>  " + os_markers[i].baths +
	  "</li><li><i class='fas fa-couch'></i>  " + os_markers[i].reception +
	  "</li></ul><h4><em> Address: " + os_markers[i].address + "</h4></em><h5><a href='" + os_markers[i].links + "'>Click here for more information</a></div>";
	  
	  var osPt = new OSRef(os_markers[i].easting,os_markers[i].northing);
      var llPt = osPt.toLatLng(osPt);
      llPt.OSGB36ToWGS84();
	  
	  addMarker(new google.maps.LatLng(llPt.lat,llPt.lng),os_markers[i].price,info)	;
	}
 }
}

function plot400450K() {
 for (var i = 0; i < os_markers.length; i++)	{ 
    if (os_markers[i].no == '8')	{	
    var info = "<div class=infowindow><h1>£" + os_markers[i].price + "</h1><h3>" + os_markers[i].address  + 
	  "</h3><ul><li><i class='fa fa-fw fa-bed'></i>  " + os_markers[i].bedrooms +
	  "</li><li><i class='fa fa-fw fa-bath'></i>  " + os_markers[i].baths +
	  "</li><li><i class='fas fa-couch'></i>  " + os_markers[i].reception +
	  "</li></ul><h4><em> Address: " + os_markers[i].address + "</h4></em><h5><a href='" + os_markers[i].links + "'>Click here for more information</a></div>";
	  
	  var osPt = new OSRef(os_markers[i].easting,os_markers[i].northing);
      var llPt = osPt.toLatLng(osPt);
      llPt.OSGB36ToWGS84();
	  
	  addMarker(new google.maps.LatLng(llPt.lat,llPt.lng),os_markers[i].price,info)	;
	}
 }
}

function plotOVER450K() {
 for (var i = 0; i < os_markers.length; i++)	{ 
    if (os_markers[i].no == '9')	{	
    var info = "<div class=infowindow><h1>£" + os_markers[i].price + "</h1><h3>" + os_markers[i].address  + 
	  "</h3><ul><li><i class='fa fa-fw fa-bed'></i>  " + os_markers[i].bedrooms +
	  "</li><li><i class='fa fa-fw fa-bath'></i>  " + os_markers[i].baths +
	  "</li><li><i class='fas fa-couch'></i>  " + os_markers[i].reception +
	  "</li></ul><h4><em> Address: " + os_markers[i].address + "</h4></em><h5><a href='" + os_markers[i].links + "'>Click here for more information</a></div>";
	  
	  var osPt = new OSRef(os_markers[i].easting,os_markers[i].northing);
      var llPt = osPt.toLatLng(osPt);
      llPt.OSGB36ToWGS84();
	  
	  addMarker(new google.maps.LatLng(llPt.lat,llPt.lng),os_markers[i].price,info)	;
	}
 }
}
