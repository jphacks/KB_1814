from item import OperateSpot, testapi, getBudget, getDistance

"""
date:[{
    region:,  0:京都、1:大阪、2:神戸　
    date_start:,unix時間
    date_end:,　unix時間
    tension:,　0:ゆっくり、1:アクティブ（インドア）、2:アクティブ（アウトドア）
    play:,　0:観光、1:ご飯（カフェ含む）、2:スポーツ
    budget:,3000:節約、10000:普通、50000:豪遊
    move:,　0:徒歩、1:電車、2:車        
}]
"""

def createResponse(data):
    return data
