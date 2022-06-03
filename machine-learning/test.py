import requests
import pandas as pd

def mergeFile():
    origin = open('data_prepare/legate2/legate_processed.txt', 'a')
    for i in range(8):
        f = open('data_prepare/legate2/legate_' + str(i) + '.txt', 'r')
        for line in f:
            origin.write(line)
        f.close
    origin.close

def addProtocol():
    file = open('data_prepare/phishing.txt', 'r')
    file2 = open('data_prepare/phishing2.txt', 'a')
    for line in file:
        file2.write('https://' + line)
    file2.close

def prepareData():
    all_result_phishing = []

    f1 = open("data_prepare/legate2/legate_processed.txt", "r")
    lines = f1.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','').split(', ')
        for j in range(len(lines[i])):
            if j>0:
                lines[i][j] = int(lines[i][j])
    f1.close()

    f2 = open("data_prepare/phishing2/phishing_processed2.txt", "r")
    legates = f2.readlines()
    for i in range(len(legates)):
        legates[i] = legates[i].replace('\n','').split(', ')
        for j in range(len(legates[i])):
            if j>0:
                legates[i][j] = int(legates[i][j])
        lines.append(legates[i])
    f2.close()
    all_result_phishing = pd.DataFrame(lines)
    all_result_phishing.to_csv('data/newProcessed.csv')

if __name__ == '__main__':
    # try:
    #     res = requests.get('http://www.bacbo.edu.vn/', timeout=5)
    # except:
    #     res = 'exp'
    # print(res)
    # mergeFile()
    prepareData()
    # addProtocol()