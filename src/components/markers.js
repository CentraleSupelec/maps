/////////////////////////////////////////////////////////////////////////////////
//////////////////////////// Add markers on the map /////////////////////////////
/////////////////////////////////////////////////////////////////////////////////

import { HOST_URL } from "../views/map.js";
import { reArrange } from "../utils/tools.js";

const createMarker = (element) => {
  var markerUrle = element.properties.style.icon;
  var markerName = element.properties.name;
  // Customize the marker icon
  var mapIcon = L.icon({
    iconUrl: "assets/icons_os/" + markerUrle,
    iconSize: [11, 11],
    iconAnchor: [5, 3],
    popupAnchor: [0, 0],
    alt: "icon",
    className: "marker_circle",
  });
  var centerPoint = reArrange(element.properties.center);
  var link =`${HOST_URL}/?id=${element.properties.id}&zoom=20`;
  var copyButtonHtml = `<button class="floorButton copy-button" onclick='
    navigator.clipboard.writeText("${link}")
      .then(()=>{this.innerHTML="Lien copié &check;"})
      .catch(()=>{alert("Impossible de copier le lien : ${link}");});
    '>Copier le lien</button>`;
  var marker = L.marker(centerPoint, { icon: mapIcon }).bindPopup(markerName +", étage "+ element.properties.floor.toString() + copyButtonHtml);
  return marker;
};

export const createMarkers = (geoJson) => {
  let markers = [];
  geoJson.features.map((element) => {
    if (element.properties.isPublished && element.properties.isVisible) {
      let marker = createMarker(element);
      markers.push(marker);
    }
  });
  return markers;
};
