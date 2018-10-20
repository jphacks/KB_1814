import requests
import json

#GoogleAPI
#PlacesAPI

# APIキーの指定
apikey = "AIzaSyCjkB7m10FzO5J7CjSaMh3r1EeErOk3eW8"

# placeid = "ChIJuzTLRwePAGARTAkpdj5blxU"     #Umie
placeid = "ChIJXeLVg9DgAGARqlIyMCX-BTY"    #USJ
# placeid = "ChIJCZEK8wimAWARi1RkteQaAh0"    #貴船神社
# placeid = "ChIJf1EXY2nnAGARN2otO_jFcKw"
# placeid = 'ChIJVVWVxPXdAGARk6J-88X_gBo'

# APIのひな型
api = "https://maps.googleapis.com/maps/api/place/details/json?&placeid={place}&key={key}"

# APIのURLを得る
url = api.format(place=placeid, key=apikey)

# 実際にAPIにリクエストを送信して結果を取得する
r = requests.get(url)

# 結果はJSON形式なのでデコードする
data = json.loads(r.text)
json_dict = data['result']
# print(type(json_dict))

print('Name：{}'.format(json_dict['name']))
print('PlaceID：{}'.format(json_dict['place_id']))

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

print('レート：{}'.format(json_dict['rating']))

print('WebSite：{}'.format(json_dict['website']))








# print json.dumps(data, sortkeys=True, indent=4)
