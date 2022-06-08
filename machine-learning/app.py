from flask import Flask, request, jsonify
from flask import Response
from flask_cors import CORS, cross_origin
import ast
import config
import base64

import URLFeatureExtraction
import MachineLearning

 
app = Flask(__name__)
 
@app.route('/url-phishing-checking', methods=['POST'])
@cross_origin()
def urlPhishingChecking():
    data = request.data.decode()
    try:
        res = ast.literal_eval(data)
        url = list(res.values())[0]
        if isBase64(url):
            url = base64.b64decode(url).decode('utf-8')
    except:
        return Response("Something went wrong!")

    input_data = URLFeatureExtraction.featureExtraction(url)
    input_data = input_data[slice(1, len(input_data))]
    result = MachineLearning.urlPhishingChecking(input_data, url)
    return jsonify(result)

def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)).decode('utf-8') == s
    except Exception:
        return False

if __name__ == '__main__':
    app.run(host='0.0.0.0')

@app.route('/', methods=['GET'])
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"