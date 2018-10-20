import requests
import json
import random

#GoogleAPI
#PlacesAPI

# タイプ，レートでスポットを絞る

# 朝，昼，晩に合わせて移動可能距離を考える
# 朝：8:00~11:00
# 昼：11:00~15:00
# 夕：15:00~18:00
# 晩：18:00~22:00


# APIキーの指定
apikey = "AIzaSyCjkB7m10FzO5J7CjSaMh3r1EeErOk3eW8"
#近隣
# api = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={range}&type={type}&key={key}"

def getspot(location, typelist, mode): #location:検索基点，typelist:検索対象type, mode:移動手段
    lat = location[0]
    lng = location[1]

    locatetype = "restaurant"

    if mode == 1:   #徒歩
        radius = "2000"
    # elif mode == 2: #車
    #     radius = 4000
    # elif mode == 3: #電車
    #     radius = 6000

    # APIのURLを得る
    # url = api.format(latitude=lat, longitude=lng, range=radius, type="restaurant", key=apikey)
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(lat) + "," + str(lng) + "&radius=" + radius + "&type=" + locatetype + "&key=" + apikey
    print(url)
    print(type(url))

    # 実際にAPIにリクエストを送信して結果を取得する
    r = requests.get(url)
    # r = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=34.665442,135.4323382&radius=2000&type=restaurant&key=AIzaSyCjkB7m10FzO5J7CjSaMh3r1EeErOk3eW8')

    # 結果はJSON形式なのでデコードする
    data = json.loads(r.text)
    json_dict = data['results']

    # 検索結果
    for spot in json_dict:
        print('Name：{}'.format(spot['name']))
        print('レート：{}'.format(spot['rating']))

    #高レートのお店をサジェスト対象とする
    spotlist = []
    print('検索対象')
    for spot in json_dict:
        if(spot['rating'] >= 4.0):
            print('Name：{}'.format(spot['name']))
            print('レート：{}'.format(spot['rating']))
            spotlist.append(spot)

    bestspot = random.choice(spotlist)

    # print(type(bestspot))

    return bestspot


def getspotdetail(spot_json):
    # APIのひな型
    api = "https://maps.googleapis.com/maps/api/place/details/json?&placeid={place}&key={key}"

    spot_dict = json.loads(spot_json)

    placeid = spot_dict['place_id']

    # APIのURLを得る
    url = api.format(place=placeid, key=apikey)
    # 実際にAPIにリクエストを送信して結果を取得する
    r = requests.get(url)

    # 結果はJSON形式なのでデコードする
    data = json.loads(r.text)
    json_dict = data['result']
    # print(type(json_dict))

    print('Name：{}'.format(json_dict['name']))
    print('Placeid：{}'.format(json_dict['place_id']))

    geo_dict = json_dict['geometry']
    print('緯度：{}'.format(geo_dict['location']['lat']))
    print('経度：{}'.format(geo_dict['location']['lng']))

    if('opening_hours' in json_dict):
        print('開園時間：')
        for time in json_dict['opening_hours']['weekday_text']:
            print(time)

    if('types' in json_dict):
        print('タイプ：')
        for type in json_dict['types']:
            print(type)

    if('rating' in json_dict):
        print('レート：{}'.format(json_dict['rating']))

    if('website' in json_dict):
        print('WebSite：{}'.format(json_dict['website']))


    spotdetail_dict ={}   #spotに関する詳細情報をまとめるdict
    spotdetail_dict["Name"] = json_dict['name']
    spotdetail_dict["PlaceId"] = json_dict['place_id']
    spotdetail_dict["Latitude"] = geo_dict['location']['lat']
    spotdetail_dict["Longitude"] = geo_dict['location']['lng']
    if('opening_hours' in json_dict):
        spotdetail_dict["OpeningHours"] = json_dict['opening_hours']['weekday_text'][0]
    if('website' in json_dict):
        spotdetail_dict["WebSite"] = json_dict['website']
    if('rating' in json_dict):
        spotdetail_dict["Types"] = json_dict['types']

    print(spotdetail_dict)
    jsondata = json.dumps(spotdetail_dict)
    # print(jsondata)

    return jsondata


#デバッグ用
if __name__ == '__main__':
    list = []
    location = [34.665442, 135.4323382]

    spot_dict = getspot(location, list, 1)
    spot_json = json.dumps(spot_dict)

    # print(type(spot_json))
    # print(spot_json)

    print('--aaa--')
    targetspot_json = getspotdetail(spot_json)

    # print(type(getspotdetail(spot_dict)))
    print('--bbb--')
    print(targetspot_json)
    # print(getspotdetail(spot_dict))

print('OK!!')
