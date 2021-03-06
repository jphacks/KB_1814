import requests
import json

def getDistance(a, b):
    origin = a
    destination = b
    url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + origin + "&destination=" + destination +"&key=AIzaSyCjkB7m10FzO5J7CjSaMh3r1EeErOk3eW8"

    headers = {"content-type": "application/json"}
    r = requests.get(url, headers=headers)
    data = r.json()
# print (json.dumps(data, indent=4))

    distance = data['routes'][0]['legs'][0]['distance']['text']
    duration = data['routes'][0]['legs'][0]['duration']['text']
    #print ("distance : " + distance)
    #print ("duration : " + duration)
    ret = [distance, duration]
    return ret

if __name__ == "__main__":
    origin = "34.702485" + "%2C" + "135.495951"
    destination = "34.654518" + "%2C" + "135.428965"
    info = getDistance(origin, destination)
    print ("distance : " + info[0])
    print ("duration : " + info[1])
