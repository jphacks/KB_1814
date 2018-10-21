from item import OperateSpot, testapi, getBudget, getDistance
# import requests
import json
# import codecs
import random
"""
date:[{
    region:,  0:京都、1:大阪、2:神戸　
    date_start:,unix時間
    date_end:,　unix時間
    tension:,　0:ゆっくり、1:アクティブ（インドア）、2:アクティブ（アウトドア）
    play:,　0:ご飯（カフェ含む）, 0:観光, 2:スポーツ
    budget:,3000:節約、10000:普通、50000:豪遊
    move:,　0:徒歩、1:電車、2:車
}]
"""

def createResponse(data):
    count = 0
    data_dict = data['data']
    print(data)

    if(count == 0):
        region = data_dict['region'][0]
        if(region == 0):
            location = [35.0037708, 135.7665593]    #河原町駅
        elif(region == 1):
            location = [34.7024854, 135.4937619]    #大阪駅
        elif(region == 2):
            location = [34.6944793, 135.1930057]    #三宮駅

    # location = [35.0037708, 135.7665593]    #河原町駅

    # type = "restaurant"

    time = data_dict['time'][0]
    tension = data_dict['tension']

    play = data_dict['play']

    index = 0
    count = 0
    allspot_dict_arry = [{}]*3
    while(1):
        toplay = data_dict['play'][index]
        # print(toplay)
        type = gettype(time, tension, toplay, index)
        # print(type)
        spot_dict = OperateSpot.getspot(location, type, 1)
        spot_json = json.dumps(spot_dict)
        targetspot_json = OperateSpot.getspotdetail(spot_json)
        spot_dict = json.loads(targetspot_json)

        # print(targetspot_json)
        allspot_dict_arry[count] = spot_dict


        if(toplay == 0): index = index +1
        count = count+1
        if(count == 3):break

    print(allspot_dict_arry)

    allspot_dict = {}
    allspot_dict['data1'] = allspot_dict_arry[0]
    allspot_dict['data2'] = allspot_dict_arry[1]
    allspot_dict['data3'] = allspot_dict_arry[2]

    jsondata = json.dumps(allspot_dict, ensure_ascii=False)

    return jsondata

def gettime(distance):
    walkv = 4       #歩く速さ4km/h
    time = distance / walkv
    return time

def gettype(time, tension, play, count):
    typefood = ['bakery', 'cafe', 'restaurant']
    typetour = ['museum']
    typeactive = ['amusement_park', 'campground', 'bowling_alley', 'casino', 'night_club', 'gym','bicycle_store', 'park', 'shopping_mall']
    typerelax = ['aquarium', 'art_gallery', 'bar', 'movie_theater','museum','clothing_store', 'department_store', 'electronics_store', 'furniture_store', 'hardware_store', 'home_goods_store', 'jewelry_store', 'library', 'movie_theater', 'pet_store', 'spa', 'store']

    if(play == 0):
        type = typefood[random.randrange(len(typefood))]
        typetime = 1
    elif(play == 1):    #観光
        type = typetour[random.randrange(len(typetour))]
        # type = 0
        # typetime = 2
    elif(play == 2 or tension == 1 or tension == 2):   #スポーツ,　アクティブ
        tmp = random.randrange(len(typeactive))
        type = typeactive[tmp]
        if tmp < 2:
            typetime = 4
        elif tmp < 7:
            typetime = 2
        else:
            typetime = 1
    else:
        tmp = random.randrange(len(typerelax))
        type = typerelax[tmp]
        if tmp < 5:
            typetime = 2
        else:
            typetime = 1

    print(type)

    return type

if __name__ == "__main__":
    jsonData = {
        'data': {
          'region':[ 2 ],
          'date': 1538406000,
          'time':[ 1 ],
          'tension': 0,
          'play': [ 0, 2 ],
          'budget': 3000,
          'move': 0
      }
    }

    data = createResponse(jsonData)

    print('------')
    print(data)
