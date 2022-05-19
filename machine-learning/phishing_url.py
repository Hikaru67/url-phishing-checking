import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

import config
import utils


def split_data():
    df = pd.read_csv(config.PATH_DATA_ALL)
    features = ['Have_IP', 'Have_At', 'URL_Length', 'URL_Depth',
                'Redirection', 'https_Domain', 'TinyURL', 'Prefix_Suffix', 'DNS_Record',
                'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over',
                'Right_Click', 'Web_Forwards']
    X = df[features]
    y = df['Label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=config.TRAINING_RATE)

    X_train.to_csv(f'{config.PATH_SAVE_DATA}/X_train.csv')
    X_test.to_csv(f'{config.PATH_SAVE_DATA}/X_test.csv')
    y_train.to_csv(f'{config.PATH_SAVE_DATA}/y_train.csv')
    y_test.to_csv(f'{config.PATH_SAVE_DATA}/y_test.csv')

    return X_train, X_test, y_train, y_test


def save_model(model):
    utils.mkdir(f'{config.PATH_SAVE_MODEL}')
    utils.save(model, f'{config.PATH_SAVE_MODEL}/model.pkl')


def model_training():
    df = pd.read_csv(config.PATH_DATA_ALL)
    features = ['Have_IP', 'Have_At', 'URL_Length', 'URL_Depth',
                'Redirection', 'https_Domain', 'TinyURL', 'Prefix_Suffix', 'DNS_Record',
                'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over',
                'Right_Click', 'Web_Forwards']
    X = df[features]
    y = df['Label']
    # X_train, X_test, y_train, y_test = split_data()
    model = CatBoostClassifier(learning_rate = 0.01, depth = 8, rsm = 1)
    model.fit(X, y)
    save_model(model)


def load_model():
    model = utils.load(f'{config.PATH_SAVE_MODEL}/model.pkl')
    return model


def predict():
    model = load_model()
    X_train, X_test, y_train, y_test = split_data()
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("Accuracy of model is: ", acc)
    print("recall of model is: ", recall)
    print("precision of model is: ", precision)
    print("f1_score of model is: ", f1)


def phishing_url():
    model = load_model()
    if model is None:

        model_training()
    else:
        model = model
    return model


def check_phishing(data):
    model = phishing_url()
    result_1 = model.predict(data)
    result_2 = model.predict_proba(data)
    return result_1, result_2


def get_phishing_url(data):
    result_1, result_2 = check_phishing(data)
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

    result.update({'label': label,
                   'suggestion': config.MODEL_SUGGESTIONS[label],
                   'Score': round(score, 2)})
    return result


if __name__ == '__main__':
    data = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0]
    print(get_phishing_url(data))
    model_training()
