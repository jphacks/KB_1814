import requests
import json
import codecs
import random

#GoogleAPI
#PlacesAPI

# タイプ，レートでスポットを絞る

# 朝，昼，晩に合わせて移動可能距離を考える
# 朝：8:00~11:00
# 昼：11:00~15:00
# 夕：15:00~18:00
# 晩：18:00~22:00


# APIキーの指定 むき出し...
apikey = "AIzaSyCjkB7m10FzO5J7CjSaMh3r1EeErOk3eW8"
# 近隣
# api = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={range}&type={type}&key={key}"

def getspot(location, type, mode): #location:検索基点，typelist:検索対象type, mode:移動手段
    lat = location[0]
    lng = location[1]

    locatetype = type

    if mode == 1:   #徒歩
        radius = "2000"
    # elif mode == 2: #車
    #     radius = 4000
    # elif mode == 3: #電車
    #     radius = 6000

    # APIのURLを得る
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(lat) + "," + str(lng) + "&radius=" + radius + "&type=" + str(locatetype) + "&key=" + apikey

    # 実際にAPIにリクエストを送信して結果を取得する
    r = requests.get(url)

    # 結果はJSON形式なのでデコードする
    data = json.loads(r.text)
    json_dict = data['results']

    # 検索結果
    # for spot in json_dict:
    #     print('Name：{}'.format(spot['name']))
    #     print('レート：{}'.format(spot['rating']))

    #高レートのお店をサジェスト対象とする
    spotlist = []
    # print('検索対象')

    for spot in json_dict:
        if('rating' in spot and spot['rating'] >= 3.0):
        # if(spot['rating'] >= 2.0):
            spotlist.append(spot)
            # print('Name：{}'.format(spot['name']))
            # print('レート：{}'.format(spot['rating']))

    if(len(spotlist) == 0): spotlist.append(spot)

    bestspot = random.choice(spotlist)
    # print(type(bestspot))

    return bestspot


def getspotdetail(spot_json):
    # APIのひな型
    api = "https://maps.googleapis.com/maps/api/place/details/json?language=ja&placeid={place}&key={key}"

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

    # print('Name：{}'.format(json_dict['name']))
    # print('Placeid：{}'.format(json_dict['place_id']))

    geo_dict = json_dict['geometry']
    # print('緯度：{}'.format(geo_dict['location']['lat']))
    # print('経度：{}'.format(geo_dict['location']['lng']))

    # if('opening_hours' in json_dict):
    #     print('開園時間：')
    #     for time in json_dict['opening_hours']['weekday_text']:
    #         print(time)
    # if('types' in json_dict):
    #     print('タイプ：')
    #     for type in json_dict['types']:
    #         print(type)
    # if('rating' in json_dict):
    #     print('レート：{}'.format(json_dict['rating']))
    # if('website' in json_dict):
    #     print('WebSite：{}'.format(json_dict['website']))

    spotdetail_dict ={}   #spotに関する詳細情報をまとめるdict
    spotdetail_dict["Name"] = json_dict['name']
    spotdetail_dict["PlaceId"] = json_dict['place_id']
    spotdetail_dict["Latitude"] = geo_dict['location']['lat']
    spotdetail_dict["Longitude"] = geo_dict['location']['lng']
    if('opening_hours' in json_dict):
        spotdetail_dict["OpeningHours"] = json_dict['opening_hours']['weekday_text']
    if('website' in json_dict):
        spotdetail_dict["WebSite"] = json_dict['website']
    if('rating' in json_dict):
        spotdetail_dict["Types"] = json_dict['types']

    print(spotdetail_dict)
    jsondata = json.dumps(spotdetail_dict, ensure_ascii=False)
    # print(jsondata)

    return jsondata


#デバッグ用
if __name__ == '__main__':
    list = []


    #targetspot_json:最初の地点から移動する先A
    #nexttargetspot_json:地点Aから移動する先B
    #next2targetspot_json:地点Bから移動する先C

    print('--aaa1--')
    # location = [34.7024854, 135.4937619]    #大阪駅
    location = [35.0037708, 135.7665593]    #河原町駅
    # location = [34.6944793, 135.1930057]    #三宮駅

    spot_dict = getspot(location, list, 1)
    spot_json = json.dumps(spot_dict)
    targetspot_json = getspotdetail(spot_json)
    print('--bbb1--')
    # print(targetspot_json)

    nextspot_dict = json.loads(targetspot_json)
    print('--aaa2--')
    nextlocation = [nextspot_dict['Latitude'], nextspot_dict['Longitude']]
    print(nextlocation[0], nextlocation[1])
    nextspot_dict = getspot(nextlocation, list, 1)
    nextspot_json = json.dumps(nextspot_dict)
    nexttargetspot_json = getspotdetail(nextspot_json)
    print('--bbb2--')

    nextnextspot_dict = json.loads(nexttargetspot_json)
    print('--aaa2--')
    nextnextlocation = [nextnextspot_dict['Latitude'], nextnextspot_dict['Longitude']]
    print(nextnextlocation[0], nextnextlocation[1])
    nextnextspot_dict = getspot(nextnextlocation, list, 1)
    nextnextspot_json = json.dumps(nextnextspot_dict)
    nextnexttargetspot_json = getspotdetail(nextnextspot_json)
    print('--bbb2--')

    goalspot_dict = json.loads(nextnexttargetspot_json)
    print('--aaa3--')
    goallocation = [goalspot_dict['Latitude'], goalspot_dict['Longitude']]

    print(location)
    print(nextlocation)
    print(nextnextlocation)
    print(goallocation)

    print(targetspot_json)
    print(nexttargetspot_json)
    print(nextnexttargetspot_json)

    allspot_dict = {}
    spot1_dict = json.loads(targetspot_json)
    spot2_dict = json.loads(nexttargetspot_json)
    spot3_dict = json.loads(nextnexttargetspot_json)

    allspot_dict.update(spot1_dict)
    allspot_dict.update(spot2_dict)
    allspot_dict.update(spot3_dict)

    jsondata = json.dumps(allspot_dict, ensure_ascii=False)
    print(jsondata)
