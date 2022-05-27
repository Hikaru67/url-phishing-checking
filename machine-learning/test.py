import requests

def mergeFile():
    origin = open('data_prepare/legate3/legate.txt', 'a')
    for i in range(4):
        f = open('data_prepare/legate3/legate_' + str(i) + '.txt', 'r')
        for line in f:
            origin.write(line)
        f.close

if __name__ == '__main__':
    # try:
    #     res = requests.get('http://www.bacbo.edu.vn/', timeout=5)
    # except:
    #     res = 'exp'
    # print(res)
    mergeFile()