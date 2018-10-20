from flask import Flask, jsonify, request
import json

import foo

app = Flask(__name__)

@app.route('/')
def hello():
    return 'ぷろじぇぇぇぇえええええええええ'

# JSON返答
@app.route('/tikeda')
def tikeda():
    return jsonify({'json':'file'})

@app.route('/tes')
def tes():
    return foo.hoge()

@app.route('/condition', methods=['POST'])
def condition():
    data = json.loads(request.data)
    print(data)
    ret = {'message':'complete'}
    return jsonify(ret)

#@app.route('/allPlans')
#def getAllPlans():
#    return html.getHtml()

def save(json):
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0')
