from xml import dom
import requests as rq
from urllib.parse import urlparse
import pandas as pd

def mergeFile():
    origin = open('data_prepare/phishing2/26_06/phishing_merged.txt', 'a')
    for i in range(6):
        f = open('data_prepare/phishing2/26_06/phishing_lost_rank' + str(i) + '.txt', 'r')
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

    f1 = open("data_prepare/webrank/legate_af_addlostft.txt", "r")
    lines = f1.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','').split(', ')
        for j in range(len(lines[i])):
            if j>0:
                lines[i][j] = int(lines[i][j])
    f1.close()

    f2 = open("data_prepare/phishing2/26_06/phishing_af_addlostft.txt", "r")
    legates = f2.readlines()
    for i in range(len(legates)):
        legates[i] = legates[i].replace('\n','').split(', ')
        for j in range(len(legates[i])):
            if j>0:
                legates[i][j] = int(legates[i][j])
        lines.append(legates[i])
    f2.close()
    all_result_phishing = pd.DataFrame(lines)
    all_result_phishing.to_csv('data/27_06/processed.csv')

def addFeature():
    lost = open("data_prepare/phishing2/26_06/phishing_merged.txt", "r")
    f1 = open("data_prepare/phishing2/phishing_processed_af.txt", "r")
    f2 = open("data_prepare/phishing2/26_06/phishing_af_addlostft.txt", "a")
    # lost = open("data_prepare/phishing2/phishing_lost0.txt", "r")
    lostObj = {}
    lostLines = lost.readlines()
    for i in range(len(lostLines)):
        lostObj[lostLines[i].split(',')[0]] = lostLines[i].split(', ')[1:]
    lines = f1.readlines()
    # linesLost = lost.readlines()
    for i in range(len(lines)):
        try:
            lines[i] = lines[i].replace('\n','').split(', ')
            # changer = lost[lines[i][0]]
            lines[i][31] = lostObj[lines[i][0]][0]
            lines[i][32] = lostObj[lines[i][0]][1]
            # for j in range(len(lines[i])):
            #     if j>0:
            lines[i][0] += ', ' + ', '.join(lines[i][1:])
            f2.writelines(lines[i][0] + '\n')
        except NameError:
            print(NameError)
    f1.close()
    f2.close()

def filterUrl():
    online = { "1337x.to": 1, "abc.go.com": 1, "adultfriendfinder.com": 1, "allrecipes.com": 1, "archiveofourown.org": 1, "atwiki.jp": 1, "avxhome.se": 1, "bigcinema.tv": 1, "bleacherreport.com": 1, "caixa.gov.br": 1, "cheezburger.com": 1, "codecanyon.net": 1, "deadspin.com": 1, "depositphotos.com": 1, "duckduckgo.com": 1, "eenadu.net": 1, "elitedaily.com": 1, "esporte.uol.com.br": 1, "fishki.net": 1, "gawker.com": 1, "gizmodo.com": 1, "graphicriver.net": 1, "hdfcbank.com": 1, "irecommend.ru": 1, "jalopnik.com": 1, "jezebel.com": 1, "khabaronline.ir": 1, "kotaku.com": 1, "likemag.com": 1, "mangafox.me": 1, "mashable.com": 1, "mediaset.it": 1, "megogo.net": 1, "mic.com": 1, "nametests.com": 1, "nguyentandung.org": 1, "noticias.uol.com.br": 1, "nypost.com": 1, "olx.pl": 1, "olx.ro": 1, "olx.ua": 1, "onedio.com": 1, "otomoto.pl": 1, "patch.com": 1, "pelis24.com": 1, "putlocker.is": 1, "sberbank.ru": 1, "seekingalpha.com": 1, "slashdot.org": 1, "stackoverflow.com": 1, "steamcommunity.com": 1, "themeforest.net": 1, "anandtech.com": 1, "arstechnica.com": 1, "ck101.com": 1, "cookpad.com": 1, "css-tricks.com": 1, "doodle.com": 1, "dribbble.com": 1, "elevenia.co.id": 1, "espn.go.com": 1, "evernote.com": 1, "fotostrana.ru": 1, "h2porn.com": 1, "himado.in": 1, "interpark.com": 1, "io9.com": 1, "lifehacker.com": 1, "mixi.jp": 1, "nymag.com": 1, "searchengines.guru": 1, "serverfault.com": 1, "skyrock.com": 1, "sputniknews.com": 1, "statcounter.com": 1, "tinypic.com": 1, "twitter.com": 1, "vnexpress.net": 1, "watch-series-tv.to": 1, "web.tv": 1, "abcnews.go.com": 1, "dealnews.com": 1, "genius.com": 1, "haraj.com.sa": 1, "jugem.jp": 1, "shareba.com": 1, "slickdeals.net": 1, "sourceforge.net": 1, "teespring.com": 1, "tympanus.net": 1, "weheartit.com": 1, "worldoftanks.ru": 1, "akhbarelyom.com": 1, "elcomercio.pe": 1, "faithtap.com": 1, "pitchfork.com": 1, "suumo.jp": 1, "getpocket.com": 1, "say-move.org": 1, "tutsplus.com": 1, "www.nhs.uk": 1, "ecnavi.jp": 1, "unity3d.com": 1, "amoory.com": 1, "weathernews.jp": 1, "wikiwiki.jp": 1, "giphy.com": 1, "myanimelist.net": 1, "huawei.com": 1, "taboola.com": 1, "udn.com": 1, "europa.eu": 1, "perezhilton.com": 1, "wmaraci.com": 1, "fanpage.gr": 1, "pantip.com": 1, "tsite.jp": 1, "auto.ru": 1, "vz.ru": 1, "hihi2.com": 1, "so-net.ne.jp": 1, "fc2.com": 1, "mirtesen.ru": 1, "livestream.com": 1, "all-free-download.com": 1, "ssa.gov": 1, "alohatube.com": 1, "kdnet.net": 1, "pinterest.com": 1, "bankmellat.ir": 1, "myegy.to": 1 }
    origin = open("data_prepare/webrank/begin.txt", "r")
    des = open("data_prepare/webrank/des2.txt", "w")
    lines = origin.readlines()
    urlSet = {}
    for i in range(len(lines)):
        try:
            domain = urlparse(lines[i]).netloc
            try: online[domain]
            except: continue
            if urlSet[domain]:
                urlSet[domain] = urlSet[domain] + 1 
                if urlSet[domain] > 100:
                    continue
                des.writelines(lines[i])
        except:
            urlSet[domain] = 1
            des.writelines(lines[i])
    des.close()

def filterHttps():
    des = open("data_prepare/webrank/des.txt", "r")
    lines = des.readlines()
    count = 0
    failureSet = {}
    for i in range(len(lines)):
        try:
            https = open("data_prepare/webrank/https.txt", "a")
            if 'https://' in lines[i]:
                des.writelines(lines[i])
                continue
            lines[i] = lines[i].replace('http://', 'https://')
            if rq.get(lines[i], timeout=5):
                count += 1
                https.writelines(lines[i])
            https.close()
        except:
            https.close()
            print(lines[i])
            domain = urlparse(lines[i]).netloc
            failureSet[lines[i]] = 1
            continue
    print(count)

def insertInMiddleOfList(list, offset, value):
    list = list[0:offset] + [value] + list[offset:]
    return list

def isDefined(val):
    try:
        if val: return 1
    except:
        return 0

if __name__ == '__main__':
    # try:
    #     res = requests.get('http://www.bacbo.edu.vn/', timeout=5)
    # except:
    #     res = 'exp'
    # print(res)
    # mergeFile()
    # appendFeature()
    prepareData()
    # addFeature()
    # addProtocol()
    # filterUrl()
    # filterHttps()