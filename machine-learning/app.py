from flask import Flask, request, jsonify
from flask import Response
from flask_cors import CORS, cross_origin
import ast
import config

import URLFeatureExtraction
import phishing_url

# from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'x3english'
# app.config['MYSQL_PASSWORD'] = 'x3english'
# app.config['MYSQL_DB'] = 'phishing'
 
# mysql = MySQL(app)

@app.route('/get_phishing_url', methods=['POST'])
@cross_origin()
def get_phishing_url():
    data = request.data.decode()
    try:
        res = ast.literal_eval(data)
        url = list(res.values())[0]
        # if url[0:8] == "https://":
        #     url = 'https:/' + url[8:]
        # elif url[0:7] == "http://":
        #     url = 'http:/' + url[7:]
    except:
        return Response("Something went wrong!")

    input_data = URLFeatureExtraction.featureExtraction(url)
    result = phishing_url.get_phishing_url(input_data)
    return jsonify(result)

@app.route('/', methods=['GET'])
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

# @app.route('/', methods=['GET'])
# @cross_origin()
# def get_phishing_url():
#     data = request.data.decode()
#     try:
#         res = ast.literal_eval(data)[i]
#         url = list(res.values())[0]
#     except:
#         return Response("Something went wrong!")

#     input_data = URLFeatureExtraction.featureExtraction(url)
#     result = phishing_url.get_phishing_url(input_data)
#     return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

