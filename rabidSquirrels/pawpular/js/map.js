var map;
var icon;
function myMap() {
    var mapOptions = {
        center: new google.maps.LatLng(42.389440, -72.526371),
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }

    map = new google.maps.Map(document.getElementById("map"), mapOptions);
    
    icon = {
        url: "pictures/camera_icon.png", // url
        scaledSize: new google.maps.Size(33, 33), // scaled size
        origin: new google.maps.Point(0,0), // origin
        anchor: new google.maps.Point(0, 0) // anchor
    };

    var catloc = new google.maps.LatLng(42.391484, -72.519467);
    var marker1 = new google.maps.Marker({
        position: catloc,
        icon: icon,
        map: map,
        title: 'Ripley\'s Cat'
    });
    var birdloc = new google.maps.LatLng(42.389562, -72.529611)
    var marker2 = new google.maps.Marker({
        position: birdloc,
        icon: icon,
        map:map,
        title: 'A Rare Friend'
    });
    var pangoloc = new google.maps.LatLng(42.399489, -72.525070);
    var marker3 = new google.maps.Marker({
        position: pangoloc,
        icon: icon,
        map:map,
        title: 'What is this?'
    });
    addInfoWindow(marker1, "<img src='pictures/cat-facehugger.jpg' width = 500px alt='1'><h2>My Child</h2><p>I love my crazy cat!!</p>");
    addInfoWindow(marker2, "<img src='pictures/Weird_bird.jpg' width = 500px alt='2'><h2>A Rare Find</h2><p>Check out this crazy bird I found!</p>")
    addInfoWindow(marker3, "<img src='pictures/pangolin.jpg' width = 500px alt='3'><h2>Help!</h2><p>What is this and why is it here???</p>")
        
    google.maps.event.addListener(map, 'click', function(event) {
        placeMarker(event.latLng);
    });
        
    setMarkers(map);
}
    
function addInfoWindow(marker, content){
    var infoWindow = new google.maps.InfoWindow({
        content: content
    });
         
    google.maps.event.addListener(marker, 'click', function () {
        infoWindow.open(map, marker);
    });
}
    
function placeMarker(location) {
    if(confirm("Confirm Marker?")) {
        var marker = new google.maps.Marker({
            position: location,
            map: map,
            icon:icon
        });
    }
}