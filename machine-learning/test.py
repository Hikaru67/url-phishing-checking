import requests

def mergeFile():
    origin = open('data_prepare/phishing/phishing_processed.txt', 'a')
    for i in range(20):
        f = open('data_prepare/phishing/phishing_' + str(i) + '.txt', 'r')
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

if __name__ == '__main__':
    # try:
    #     res = requests.get('http://www.bacbo.edu.vn/', timeout=5)
    # except:
    #     res = 'exp'
    # print(res)
    mergeFile()
    # addProtocol()