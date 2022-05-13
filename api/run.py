from flask import Flask, request, jsonify
from flask import Response
from flask_cors import CORS, cross_origin
import ast

import URLFeatureExtraction
import phishing_url

app = Flask(__name__)

@app.route('/get_phishing_url', methods=['POST'])
@cross_origin()
def get_phishing_url():
    data = request.data.decode()
    try:
        res = ast.literal_eval(data)
        url = list(res.values())[0]
    except:
        return Response("Json Error!")

    input_data = URLFeatureExtraction.featureExtraction(url)
    result = phishing_url.get_phishing_url(input_data)
    return jsonify(result)

if __name__ == '__main__':
    app.run('127.0.0.1', port=5001)

