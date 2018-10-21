import requests
import json

def getBudget(a, b, c):
    latitude = a
    longitude = b
    name = c
    url = "https://api.gnavi.co.jp/RestSearchAPI/20150630/?keyid=264a257d88e6a732c7195178e8f86f90&format=json&latitude=" + latitude + "&longitude="+ longitude +"&name=" + name

    headers = {"content-type": "application/json"}
    r = requests.get(url, headers=headers)
    data = r.json()
    print("aaaa")
    # print (json.dumps(data, indent=4))

    budget = data['rest']['budget']
    lunch = data['rest']['lunch']
    if budget != {}:
        print ("budget : " + budget + "円")

    if lunch != {}:
        print ("lunch : " + lunch + "円")

if __name__ == "__name__":
    latitude = "34.702492"
    longitude = "135.4959658"
    name = "UMEDAI Garden Restaurant"
    getBudget(latitude, longitude, name)
