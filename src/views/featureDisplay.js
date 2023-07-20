/////////////////////////////////////////////////////////////////////////////////
///////////////////////// Add interactions with the map /////////////////////////
/////////////////////////////////////////////////////////////////////////////////

import { map, HOST_URL } from "../views/map.js";

export const filter = (feature) => {
  // Filter the features to be displayed
  return feature.properties.isVisible && feature.properties.isPublished;
};

export const style = (feature) => {
  // Style the features with their
  return feature.properties.style;
};

const zoomToFeature = (e) => {
  // Zoom to *polygon* feature when clicked
  map.fitBounds(e.target.getBounds());
};

const zoomToFeaturePoint = (e) => {
  // Zoom to *point* feature when clicked
  map.setView([e.latlng.lat, e.latlng.lng], 19);
};

const highlightFeature = (e) => {
  // Highlight feature when mouseover or mousedown
  var layer = e.target;
  layer.setStyle({
    weight: 5,
    color: "#666",
    dashArray: "",
    fillOpacity: 0.7,
  });
  if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
    layer.bringToFront();
  }
  //info.update(layer.feature.properties);
};

const resetHighlight = (e) => {
  // Reset feature style after being Highlighted
  var layer = e.target;
  layer.setStyle(style(layer.feature));
};

export const onEachFeature = (feature, layer) => {
  // Make the feature clickable if so
  if (feature.properties.isClickable) {
    var link =`${HOST_URL}/?id=${feature.properties.id}&zoom=20`;
    var copyButtonHtml = `<button class="floorButton copy-button" onclick='
      navigator.clipboard.writeText("${link}")
        .then(()=>{this.innerHTML="Lien copié &check;"})
        .catch(()=>{alert("Impossible de copier le lien : ${link}");});
      '>Copier le lien</button>`;
  
    layer.bindPopup(feature.properties.name+", étage "+feature.properties.floor.toString()+copyButtonHtml);
    if (feature.geometry.type == "Polygon") {
      layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature,
      });
    } else if (feature.geometry.type == "Point") {
      layer.on({
        click: zoomToFeaturePoint,
      });
    }
  }
};
