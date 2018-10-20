from flask import Flask, jsonify, request
import json

import res, htmlGen

app = Flask(__name__)

# JSON返答
@app.route('/tikeda')
def tikeda():
    return jsonify({'json':'file'})

@app.route('/condition', methods=['POST'])
def condition():
    data = json.loads(request.data)
    ret = res.createResponse(data)
    """
    ret = {
        'Name': '十二段家 本店', 
        'PlaceId': 'ChIJP7SncMEIAWARAzHg_D_VLG0', 
        'Latitude': 35.002993, 
        'Longitude': 135.775346,
        'OpeningHours': '月曜日: 11時30分～13時30分, 17時00分～20時00分', 
        'WebSite': 'http://junidanya-kyoto.com/', 
            'Types': ['restaurant', 'food', 'point_of_interest', 'establishment']
    }
    """
    return jsonify(ret)

@app.route('/allPlans')
def getAllPlans():
    return htmlGen.getHtml()

def save(json):
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0')
