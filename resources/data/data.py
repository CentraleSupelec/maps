import json
import codecs
import csv
import numpy as np
import os

############################################################################################################
############################################## Move a feature ##############################################
############################################################################################################

def moveElement(coordinates, toLeft, toRight, toTop, toBottom):
    ''' Function to move a feature's position to the left, right, top or bottom'''
    newCoord = []
    n = len(coordinates)
    if n > 1:  # Same as feature["geometry"]["type"] == "Point"
        # coord = feature["geometry"]["coordinates"]
        coord = coordinates
        newCoord = [coord[0] - toLeft + toRight, coord[1] + toTop - toBottom]
        # print(coord)
        # print(newCoord)
        return newCoord
    elif n == 1:  # same as feature["geometry"]["type"] == "Polygon"
        # for coord in feature["geometry"]["coordinates"][0]:
        for coord in coordinates[0]:
            newCoord.append([coord[0] - toLeft + toRight,
                            coord[1] + toTop - toBottom])
        return [newCoord]

# Move the features to the right, left, top or bottom. Only translations are done.
moveTo = {
    "bouygues": {
                "0": {
                    "toLeft": 0.0000,
                    "toRight": 0.0000,
                    "toTop": 0.0000,
                    "toBottom": 0.000050,
                },
                "1": {
                    "toLeft": 0.0000,
                    "toRight": 0.0000,
                    "toTop": 0.0000,
                    "toBottom": 0.000050,
                },
                "2": {
                    "toLeft": 0.0000,
                    "toRight": 0.0000,
                    "toTop": 0.0000,
                    "toBottom": 0.000050,
                },
                },
    "breguet": {
                "0": {
                    "toLeft": 0.0000,
                    "toRight": 0.000022,
                    "toTop": 0.000050,
                    "toBottom": 0.0000,
                },
                "1": {
                    "toLeft": 0.0000,
                    "toRight": 0.000022,
                    "toTop": 0.000050,
                    "toBottom": 0.0000,
                },
                "2": {
                    "toLeft": 0.0000,
                    "toRight": 0.000022,
                    "toTop": 0.000050,
                    "toBottom": 0.0000,
                },
                "3": {
                    "toLeft": 0.0000,
                    "toRight": 0.000006,
                    "toTop": 0.000086,
                    "toBottom": 0.0000,
                },
                "4": {
                    "toLeft": 0.0000,
                    "toRight": 0.000006,
                    "toTop": 0.000086,
                    "toBottom": 0.0000,
                },
                },
    "eiffel": {
                "0": {
                    "toLeft": 0.0000,
                    "toRight": 0.0000,
                    "toTop": 0.0000,
                    "toBottom": 0.0000,
                },
                "1": {
                    "toLeft": 0.0000,
                    "toRight": 0.0000,
                    "toTop": 0.0000,
                    "toBottom": 0.0000,
                },
                "2": {
                    "toLeft": 0.0000,
                    "toRight": 0.0000,
                    "toTop": 0.0000,
                    "toBottom": 0.0000,
                },
                "3": {
                    "toLeft": 0.0000,
                    "toRight": 0.0000,
                    "toTop": 0.0000,
                    "toBottom": 0.0000,
                },
                "4": {
                    "toLeft": 0.0000,
                    "toRight": 0.0000,
                    "toTop": 0.0000,
                    "toBottom": 0.0000,
                },
                },
    "metz": {
                "-1": {
                    "toLeft": 0.0000,
                    "toRight": 0.0000,
                    "toTop": 0.0000,
                    "toBottom": 0.0000,
                },
                "0": {
                    "toLeft": 0.0000,
                    "toRight": 0.0000,
                    "toTop": 0.0000,
                    "toBottom": 0.0000,
                },
                "1": {
                    "toLeft": 0.0000,
                    "toRight": 0.0000,
                    "toTop": 0.0000,
                    "toBottom": 0.0000,
                },
                "2": {
                    "toLeft": 0.0000,
                    "toRight": 0.0000,
                    "toTop": 0.0000,
                    "toBottom": 0.0000,
                },
                "3": {
                    "toLeft": 0.0000,
                    "toRight": 0.0000,
                    "toTop": 0.0000,
                    "toBottom": 0.0000,
                },
                },
}

def moveBuildingElement(building, feature):
    ''' Function to move a feature's position according to its building & its floor'''
    coord = feature["geometry"]["coordinates"]
    floor = feature["properties"]["floor"]
    if building == "none":
        return coord
    elif building != "none":
        return moveElement(
            coord,
            moveTo[building][str(floor)]["toLeft"],
            moveTo[building][str(floor)]["toRight"],
            moveTo[building][str(floor)]["toTop"],
            moveTo[building][str(floor)]["toBottom"]
            )

############################################################################################################
#################################### Tag a feature with its building #######################################
############################################################################################################

def testInBuilding(coord,
                    # name
                    ):
    '''Function that returns the building to which the *point* of a feature is in'''
    bouygues = {'left': 2.166293, 'right': 2.168535,
                'top': 48.709629, 'bottom': 48.708691}
    breguet = {'left': 2.162686, 'right': 2.16535,
                'top': 48.709302, 'bottom': 48.707812}
    eiffel = {'left': 2.166521, 'right': 2.168695,
                'top': 48.710906, 'bottom': 48.709786}
    metz = {'left': 6.220099, 'right': 6.22174,
            'top': 49.103887, 'bottom': 49.102544}
    if bouygues["left"] < coord[0] < bouygues["right"] and bouygues["bottom"] < coord[1] < bouygues["top"]:
        return "bouygues"
    elif breguet["left"] < coord[0] < breguet["right"] and breguet["bottom"] < coord[1] < breguet["top"]:
        return "breguet"
    elif eiffel["left"] < coord[0] < eiffel["right"] and eiffel["bottom"] < coord[1] < eiffel["top"]:
        return "eiffel"
    elif metz["left"] < coord[0] < metz["right"] and metz["bottom"] < coord[1] < metz["top"]:
        return "metz"
    # print(name + " is not in any building")
    return "none"

def tagBuilding(feature):
    '''Function that returns the building to which the *feature* is in'''
    polygonPointsBuildings = []  # List of the building of each point in the polygon
    #name = feature["properties"]["name"]
    if feature["geometry"]["type"] == "Point":
        return testInBuilding(feature["geometry"]["coordinates"], 
        #name
        )
    elif feature["geometry"]["type"] == "Polygon":
        for coord in feature["geometry"]["coordinates"][0]:
            polygonPointsBuildings.append(testInBuilding(coord, 
            #name
            ))
        i = 0
        n = len(polygonPointsBuildings)
        while i < n or polygonPointsBuildings[0] == polygonPointsBuildings[i]:
            i += 1
            if i == n:
                break
        if i == n:  # If all the elements are in the same building return the building
            return polygonPointsBuildings[0]
        #print(name + " is not in any building")
        return "none"

############################################################################################################
################### Template a feature's data in the final GeoJSON & the search GeoJSON ####################
############################################################################################################

def giveMeData(type, geometryType, geometryCoordinates, id, name, alias, floor, isPublished, isSearchable, isVisible, isClickable, style, placeType, translations, center, building):
    '''Define feature with a syntax compatible with leaflet and the front-end code'''
    feature = {
        "type": type,
        "geometry": {
            "type": geometryType,
            "coordinates": geometryCoordinates
        },
        "properties": {
            "id": id,
            "name": name,
            "alias": alias,
            "floor": floor,
            "isPublished": isPublished,
            "isSearchable": isSearchable,
            "isVisible": isVisible,
            "isClickable": isClickable,
            "style": style,
            "placeType": placeType,
            "translations": translations,
            "center": center,
            "building": building
        }
    }
    return feature

def searchForElement(type, geometryType, geometryCoordinates, id,
                        # name, alias,
                        floor,
                        #  isPublished, isSearchable, isVisible, isClickable, style, placeType, translations,center,
                        popupContent, title, description, icon):
    '''Define feature with the keys required for the search box'''
    feature = {
        "type": type,
        "geometry": {
            "type": geometryType,
            "coordinates": geometryCoordinates
        },
        "properties": {
            "id": id,
            # "name": name,
            # "alias": alias,
            "floor": floor,
            # "isPublished": isPublished,
            # "isSearchable": isSearchable,
            # "isVisible": isVisible,
            # "isClickable": isClickable,
            # "style": style,
            # "placeType": placeType,
            # "translations": translations,
            # "center": center,
            "popupContent": popupContent,
            "title": title,
            "description": description,
            "image": icon
        }
    }
    return feature

def searchForElementByURL(
                        # type, geometryType, geometryCoordinates, 
                        id,
                        name, 
                        # alias,
                        floor,
                        #  isPublished, isSearchable, isVisible, isClickable, style, placeType, translations,
                        center,
                        # popupContent, title, description, icon
                        location):
    '''Define feature with the keys required for the search box'''
    feature = {
        # "type": type,
        # "geometry": {
        #     "type": geometryType,
        #     "coordinates": geometryCoordinates
        # },
        "properties": {
            "id": id,
            "name": name,
            # "alias": alias,
            "floor": floor,
            # "isPublished": isPublished,
            # "isSearchable": isSearchable,
            # "isVisible": isVisible,
            # "isClickable": isClickable,
            # "style": style,
            # "placeType": placeType,
            # "translations": translations,
            "center": center,
            # "popupContent": popupContent,
            # "title": title,
            # "description": description,
            # "image": icon
            "location": location
        }
    }
    return feature

############################################################################################################
################################################ Tools #####################################################
############################################################################################################

def iconName(icon_name):
    '''Function that returns the icon url from the feature placeType propertie'''
    icon_name1 = icon_name.translate(str.maketrans({" ": "_", "[": "", ".": "", ",": "", "|": "", "/": "", "#": "", "!": "", "$": "", "%": "", "^": "",
                                        "&": "", "*": "", ";": "", ":": "", "{": "", "}": "", "=": "", "'": "",  "-": "", "`": "", "~": "", "(": "", ")": "", "]": "", "@": "", "+": ""}))
    icon_name2 = icon_name1.lower()
    return icon_name2+".svg"

def createJson(campus, floors):
    '''Function that creates a dictionary with floors GeoJsons'''
    floorsJsons = {}
    for floor in floors:
        floorsJsons[str(campus)+"_"+str(floor)] = {"type": "FeatureCollection", "features": []}
    return floorsJsons

############################################################################################################
###################### Main function to generate all the needed data for the Web app #######################
############################################################################################################

def generateCompatibleJson(path, json_output, search_json, campus, floors):
    '''Use MapWize's GeoJson to generate better GeoJson files for leaflet and csv for AppScho'''
    
    # The newGeoJson that is more compatible with leaflet library
    newGeoJson = {
        "type": "FeatureCollection",
        "features": []}

    # Create a dictionary of floors with their corresponding GeoJSON
    floorsJsons = createJson(campus, floors)

    # The CSV listing the features with their IDs and URLs
    forAppScho = []

    # The searchJson for the search box
    searchJson = {
        "type": "FeatureCollection",
        "features": []}

        # Search by URL GeoJSON
    searchJsonByURL = {
        "type": "FeatureCollection",
        "features": []}

    # Open icons.json that defines the style and the icon corresponding to a specific placeType
    with codecs.open('icons.json', 'r+', encoding='utf-8') as file1:
        markerCollection = json.load(file1)

    # Open the base MapWize GeoJSON
    with codecs.open(path, 'r+', encoding='utf-8') as file2:
        data = json.load(file2)

        # Iterate on features
        for feature in data["features"]:

            # Iterate on markers
            for marker in markerCollection["markers"]:

                # Selecting the features having a marker (basically all of them) and those in the default universe (as the Oraux 2019 universe is useless)
                if iconName(feature["properties"]["placeType"]) == marker["icon"] and feature["properties"]["universes"][0] == "Default universe":
                    
                    # Feature floor
                    featureFloor=feature["properties"]["floor"]

                    # Tag the feature with its building
                    featureBuilding = tagBuilding(feature)

                    # Change the elements' coordinates by by moving the element's position according to the values defined in the moveBuildingElement function
                    coordinates = moveBuildingElement(featureBuilding,
                        feature)
                    
                    centerPoint = []
                    # If the feature is a Polygon, find its center to place the marker later on
                    if feature["geometry"]["type"] == "Polygon":
                        poly = coordinates[0][:]
                        newPoly = np.array(poly)
                        centroid = newPoly.mean(axis=0)
                        centerPoint = list(centroid)
                    # If the feature is a Point, its center is its deafult coordinates
                    elif feature["geometry"]["type"] == "Point":
                        centerPoint = coordinates

                    # Create a feature
                    details = giveMeData(
                        type=feature["type"],
                        geometryType=feature["geometry"]["type"],
                        geometryCoordinates=coordinates,
                        id=feature["properties"]["id"],
                        name=feature["properties"]["name"],
                        alias=feature["properties"]["alias"],
                        floor=featureFloor,
                        isPublished=feature["properties"]["isPublished"],
                        isSearchable=feature["properties"]["isSearchable"],
                        isVisible=feature["properties"]["isVisible"],
                        isClickable=feature["properties"]["isClickable"],
                        style=marker,
                        placeType=feature["properties"]["placeType"],
                        translations=feature["properties"]["translations"],
                        center=centerPoint,
                        # Add building attribute to the feature
                        building=featureBuilding
                    )

                    # Add the feature to the GeoJSON
                    newGeoJson["features"].append(details)

                    # Add the feature the corresponding floor json
                    floorsJsons[campus+"_"+str(featureFloor)]["features"].append(details)

                    if feature["properties"]["isSearchable"]:
                        # Create a search element for the feature
                        searchElements = searchForElement(
                            type=feature["type"],
                            geometryType=feature["geometry"]["type"],
                            geometryCoordinates=coordinates,
                            id=feature["properties"]["id"],
                            floor=featureFloor,
                            popupContent=feature["properties"]["name"]+", Étage "+str(featureFloor) if featureBuilding != "none" else feature["properties"]["name"],
                            title=feature["properties"]["name"],
                            description=feature["properties"]["translations"][0]["subtitle"],
                            icon=marker["icon"],
                        )

                        # Add the search element to the searchJSON
                        searchJson["features"].append(searchElements)

                        # Add a line in the CSV file designating the feature
                        forAppScho.append({ 
                            "campus": campus,
                            "name": feature["properties"]["name"],
                            "id": feature["properties"]["id"],
                            "url_id": "https://maps.centralesupelec.fr/?id="+feature["properties"]["id"]+"&zoom=20",
                            "alias": feature["properties"]["alias"],
                            "url_alias": "https://maps.centralesupelec.fr/?alias="+feature["properties"]["alias"]+"&zoom=20",
                        })

                        # Create a URL searchable element for the feature
                        searchElementsByURL = searchForElementByURL(
                            id=feature["properties"]["id"],
                            name=feature["properties"]["name"],
                            floor=featureFloor,
                            center=centerPoint,
                            location=campus,
                        )
                        searchJsonByURL["features"].append(searchElementsByURL)

        # print(len(data["features"]))
        # print("Removing oraux 2019 universe for PS")
        # print(len(newGeoJson["features"]))
        # print(len(forAppScho))
        # print(len(searchJson["features"]))

    # Export the GeoJSON
    with codecs.open(json_output+"campusmap_cs_"+campus+".json", 'w', encoding='utf-8') as jsonFile1:
        json.dump(newGeoJson, jsonFile1, indent=4, ensure_ascii=False)

    # Export the searchJSON
    with codecs.open(search_json, 'w', encoding='utf-8') as jsonFile2:
        json.dump(searchJson, jsonFile2, indent=4, ensure_ascii=False)

    # Export the floors
    for floor in floorsJsons:
        with codecs.open(json_output+'cs_'+floor+".json", 'w', encoding='utf-8') as jsonFile3:
            json.dump(floorsJsons[floor], jsonFile3, indent=4, ensure_ascii=False)
    
    return searchJsonByURL, forAppScho

############################################################################################################
############################## Generate the data by uncommenting what follows ##############################
############################################################################################################

# generateCompatibleJson("./mapwize_cs_ps.json", '../../src/data/cs_',
#                         'cs_ps_features.csv', '../../src/data/cs_ps_search.json', "ps", [0,1,2,3,4])
# generateCompatibleJson("./mapwize_cs_metz.json", '../../src/data/cs_',
#                         'cs_metz_features.csv', '../../src/data/cs_metz_search.json', "metz", [-1,0,1,2,3])

def generateEverything():
    if not os.path.exists("./generated"):
        os.mkdir("./generated")
    searchJson, forAppScho = generateCompatibleJson("./mapwize/mapwize_cs_ps.json", './generated/',
                        './generated/cs_ps_search.json', "ps", [0,1,2,3,4])
    addToSearchJson, addToforAppScho = generateCompatibleJson("./mapwize/mapwize_cs_metz.json", './generated/',
                        './generated/cs_metz_search.json', "metz", [-1,0,1,2,3])

    searchJson["features"].extend(addToSearchJson["features"])
    with codecs.open("./generated/cs_searchByURL.json", 'w', encoding='utf-8') as jsonFile4:
        json.dump(searchJson, jsonFile4, indent=4, ensure_ascii=False) 

    forAppScho.extend(addToforAppScho)
    # Export the CSV
    with open('./generated/cs_features_data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Campus', 'Name', 'ID', 'URL with ID', 'Alias', 'URL with Alias'])  # header row
        for element in forAppScho:
            writer.writerow(element.values())    


generateEverything()