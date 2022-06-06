import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier, VotingClassifier

import config
import utils


def splitData():
    df = pd.read_csv(config.PATH_DATA_ALL)
    features = [
        'Domain_Length',
        'Subdomain_Level',
        # 'Url_Length',
        'Have_At_Sign',
        'Have_Tilde_Symbol',
        'No_Https',
        'Having_IP',
        'Domain_In_Subdomains',
        'Domain_In_Paths',
        'Http_In_Hostname',
        'Double_Slash_In_Path',
        'Num_Dots',
        'Num_Dashes_In_Hostname',
        'Num_Underscore',
        'Num_Percent',
        'Num_Query_Components',
        'Num_Ampersand',
        'Num_Hash',
        'Num_Numeric_Chars',
        # 'Path_Length',
        # 'Query_Length',
        'Num_Sensitive_Words',
        'Ext_Favicon',
        'Redirection',
        'Tiny_URL',
        'Prefix_Suffix',
        'DNS',
        'Domain_Age',
        'Domain_End',
        'Rank_Host',
        'Rank_Country',
        'Iframe',
        'Mouse_Over',
        'Right_Click',
        'Forwarding'
    ]
    X = df[features]
    y = df['Label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)

    X_train.to_csv(f'{config.PATH_SAVE_DATA}/X_train.csv')
    X_test.to_csv(f'{config.PATH_SAVE_DATA}/X_test.csv')
    y_train.to_csv(f'{config.PATH_SAVE_DATA}/y_train.csv')
    y_test.to_csv(f'{config.PATH_SAVE_DATA}/y_test.csv')

    return X_train, X_test, y_train, y_test

def save_model(model):
    utils.mkdir(f'{config.PATH_SAVE_MODEL}')
    utils.save(model, f'{config.PATH_SAVE_MODEL}/model.pkl')

def trainModel():
    df = pd.read_csv(config.PATH_DATA_ALL)
    features = ['Domain_Length','Subdomain_Level','Have_At_Sign','Have_Tilde_Symbol','No_Https','Having_IP','Domain_In_Subdomains','Domain_In_Paths','Http_In_Hostname','Double_Slash_In_Path','Num_Dots','Num_Dashes_In_Hostname','Num_Underscore','Num_Percent','Num_Query_Components','Num_Ampersand','Num_Hash','Num_Numeric_Chars','Num_Sensitive_Words','Ext_Favicon','Redirection','Tiny_URL','Prefix_Suffix','DNS','Domain_Age','Domain_End','Rank_Host','Rank_Country','Iframe','Mouse_Over','Right_Click','Forwarding']
    X = df[features]
    y = df['Label']
    model = CatBoostClassifier(learning_rate = 0.1, depth = 8, rsm = 1)
    model.fit(X, y)
    save_model(model)

def loadModel():
    model = utils.load(f'{config.PATH_SAVE_MODEL}/model.pkl')
    return model

def predict():
    model = loadModel()
    X_train, X_test, y_train, y_test = splitData()
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("Accuracy of model is: ", acc)
    print("recall of model is: ", recall)
    print("precision of model is: ", precision)
    print("f1_score of model is: ", f1)

def getModel():
    model = loadModel()
    if model is None:

        trainModel()
    else:
        model = model
    return model

def getResult(data):
    model = getModel()
    result_1 = model.predict(data)
    result_2 = model.predict_proba(data)
    return result_1, result_2

def urlPhishingChecking(data):
    result_1, result_2 = getResult(data)
    if result_1 == 1:
        label = 'bad'
    else:
        label = 'good'
    print(result_2)
    flag = np.argmax(result_2)
    if flag == 0:
        score = result_2[0] * 100
    elif flag == 1:
        score = result_2[1] * 100

    result = {}

    result.update({
        'label': label,
        'suggestion': config.MODEL_SUGGESTIONS[label],
        'percent': round(score, 2),
        'features': data
    })
    return result

if __name__ == '__main__':
    # data = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0]
    # print(urlPhishingChecking(data))
    trainModel()
