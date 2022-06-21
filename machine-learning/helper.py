import requests
import pandas as pd

def mergeFile():
    origin = open('data_prepare/webrank/legate_processed.txt', 'a')
    for i in range(6):
        f = open('data_prepare/webrank/legate_' + str(i) + '.txt', 'r')
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

    f1 = open("data_prepare/legate2/legate_processed2.txt", "r")
    lines = f1.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','').split(', ')
        for j in range(len(lines[i])):
            if j>0:
                lines[i][j] = int(lines[i][j])
    f1.close()

    f2 = open("data_prepare/phishing2/phishing_processed22.txt", "r")
    legates = f2.readlines()
    for i in range(len(legates)):
        legates[i] = legates[i].replace('\n','').split(', ')
        for j in range(len(legates[i])):
            if j>0:
                legates[i][j] = int(legates[i][j])
        lines.append(legates[i])
    f2.close()
    all_result_phishing = pd.DataFrame(lines)
    all_result_phishing.to_csv('data/newProcessed22.csv')

def addFeature():
    f1 = open("data_prepare/webrank/legate_processed.txt", "r")
    f2 = open("data_prepare/webrank/legate_processed_af.txt", "a")
    lost = open("data_prepare/webrank/legate_lost0.txt", "r")
    lines = f1.readlines()
    linesLost = lost.readlines()
    for i in range(len(lines)):
        # print(lines[i])
        lines[i] = lines[i].replace('\n','').split(', ')
        linesLost[i] = linesLost[i].replace('\n','').split(', ')
        lines[i][2] += ', ' + linesLost[i][1] + ', 0'
        lines[i][18] += ', 0, 0'
        for j in range(len(lines[i])):
            if j>0:
                lines[i][0] += ', ' + lines[i][j]
        f2.writelines(lines[i][0] + '\n')
    f1.close()
    f2.close()

def appendFeature():
    origin = open("data_prepare/webrank/legate_processed.txt", "r")
    lost = open("data_prepare/webrank/legate_lost0.txt", "r")
    linesOrigin = origin.readlines()
    linesLost = origin.readlines()
    for i in range(len(linesOrigin)):
        linesOrigin[i] = linesOrigin[i].replace('\n','').split(', ')
        linesLost[i] = linesLost[i].replace('\n','').split(', ')
        if (linesOrigin[i][0] == linesLost[i][0]):
            linesOrigin[i][2] = linesOrigin[i][2] + ', ' + linesLost[i][1] + ', ' + linesLost[i][2]
    # for i in range(len(lines)):
    #     # print(lines[i])
    #     lines[i] = lines[i].replace('\n','').split(', ')
    #     lines[i][2] += ', ' + str(len(lines[i][0]))
    #     for j in range(len(lines[i])):
    #         if j>0:
    #             lines[i][0] += ', ' + lines[i][j]
        # f2.writelines(lines[i][0] + '\n')
    origin.close()
    lost.close()

def insertInMiddleOfList(list, offset, value):
    list = list[0:offset] + [value] + list[offset:]
    return list

if __name__ == '__main__':
    # try:
    #     res = requests.get('http://www.bacbo.edu.vn/', timeout=5)
    # except:
    #     res = 'exp'
    # print(res)
    # mergeFile()
    # appendFeature()
    # prepareData()
    addFeature()
    # addProtocol()