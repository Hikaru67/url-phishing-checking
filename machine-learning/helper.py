from xml import dom
import requests as rq
from urllib.parse import urlparse
import pandas as pd

def mergeFile():
    origin = open('data_prepare/webrank/legate_processed.txt', 'a')
    for i in range(5):
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

    f1 = open("data_prepare/webrank/legate_processed_af.txt", "r")
    lines = f1.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','').split(', ')
        for j in range(len(lines[i])):
            if j>0:
                lines[i][j] = int(lines[i][j])
    f1.close()

    f2 = open("data_prepare/phishing2/phishing_processed_af.txt", "r")
    legates = f2.readlines()
    for i in range(len(legates)):
        legates[i] = legates[i].replace('\n','').split(', ')
        for j in range(len(legates[i])):
            if j>0:
                legates[i][j] = int(legates[i][j])
        lines.append(legates[i])
    f2.close()
    all_result_phishing = pd.DataFrame(lines)
    all_result_phishing.to_csv('data/ProcessedHasWebRank.csv')

def addFeature():
    lost = { "1337x.to": [ "1337x.to", "0", "1", "1", "0", "0", "0" ], "abc.go.com": [ "abc.go.com", "0", "0", "0", "0", "0", "0" ], "adultfriendfinder.com": [ "adultfriendfinder.com", "0", "0", "1", "0", "0", "0" ], "allrecipes.com": [ "allrecipes.com", "0", "0", "0", "0", "0", "0" ], "archiveofourown.org": [ "archiveofourown.org", "0", "0", "0", "0", "0", "0" ], "atwiki.jp": [ "atwiki.jp", "0", "1", "1", "0", "0", "0" ], "avxhome.se": [ "avxhome.se", "0", "0", "0", "0", "0", "0" ], "bigcinema.tv": [ "bigcinema.tv", "0", "0", "1", "0", "-1", "0" ], "bleacherreport.com": [ "bleacherreport.com", "0", "0", "0", "0", "0", "0" ], "caixa.gov.br": [ "caixa.gov.br", "0", "1", "1", "0", "0", "0" ], "cheezburger.com": [ "cheezburger.com", "0", "0", "0", "0", "0", "0" ], "codecanyon.net": [ "codecanyon.net", "0", "0", "0", "0", "0", "0" ], "deadspin.com": [ "deadspin.com", "0", "0", "1", "0", "0", "0" ], "depositphotos.com": [ "depositphotos.com", "0", "0", "0", "0", "0", "0" ], "duckduckgo.com": [ "duckduckgo.com", "0", "0", "0", "0", "0", "0" ], "eenadu.net": [ "eenadu.net", "0", "0", "0", "0", "0", "0" ], "elitedaily.com": [ "elitedaily.com", "0", "0", "0", "0", "0", "0" ], "esporte.uol.com.br": [ "esporte.uol.com.br", "0", "1", "0", "0", "-1", "0" ], "fishki.net": [ "fishki.net", "0", "0", "0", "0", "0", "0" ], "gawker.com": [ "gawker.com", "0", "0", "0", "0", "0", "0" ], "gizmodo.com": [ "gizmodo.com", "0", "0", "1", "0", "0", "0" ], "graphicriver.net": [ "graphicriver.net", "0", "0", "0", "0", "0", "0" ], "hdfcbank.com": [ "hdfcbank.com", "0", "0", "0", "0", "0", "0" ], "irecommend.ru": [ "irecommend.ru", "0", "0", "0", "0", "0", "0" ], "jalopnik.com": [ "jalopnik.com", "0", "0", "1", "0", "0", "0" ], "jezebel.com": [ "jezebel.com", "0", "0", "0", "0", "0", "0" ], "khabaronline.ir": [ "khabaronline.ir", "0", "1", "1", "0", "0", "0" ], "kotaku.com": [ "kotaku.com", "0", "0", "0", "0", "0", "0" ], "likemag.com": [ "likemag.com", "0", "0", "1", "-1", "-1", "0" ], "mangafox.me": [ "mangafox.me", "0", "0", "0", "0", "0", "0" ], "mashable.com": [ "mashable.com", "0", "0", "0", "0", "0", "0" ], "mediaset.it": [ "mediaset.it", "0", "0", "1", "0", "0", "0" ], "megogo.net": [ "megogo.net", "0", "0", "0", "0", "0", "0" ], "mic.com": [ "mic.com", "0", "0", "0", "0", "0", "0" ], "nametests.com": [ "nametests.com", "0", "0", "0", "0", "-1", "0" ], "nguyentandung.org": [ "nguyentandung.org", "0", "0", "1", "1", "-1", "0" ], "noticias.uol.com.br": [ "noticias.uol.com.br", "0", "1", "0", "0", "0", "0" ], "nypost.com": [ "nypost.com", "0", "0", "1", "0", "0", "0" ], "olx.pl": [ "olx.pl", "0", "0", "1", "0", "0", "0" ], "olx.ro": [ "olx.ro", "0", "0", "1", "0", "0", "0" ], "olx.ua": [ "olx.ua", "0", "1", "0", "0", "0", "0" ], "onedio.com": [ "onedio.com", "0", "0", "0", "0", "0", "0" ], "otomoto.pl": [ "otomoto.pl", "0", "0", "0", "0", "0", "0" ], "patch.com": [ "patch.com", "0", "0", "0", "0", "0", "0" ], "pelis24.com": [ "pelis24.com", "0", "0", "0", "0", "-1", "0" ], "putlocker.is": [ "putlocker.is", "0", "1", "1", "0", "0", "0" ], "sberbank.ru": [ "sberbank.ru", "0", "0", "1", "0", "0", "0" ], "seekingalpha.com": [ "seekingalpha.com", "0", "0", "1", "0", "0", "0" ], "slashdot.org": [ "slashdot.org", "0", "0", "0", "0", "0", "0" ], "stackoverflow.com": [ "stackoverflow.com", "0", "0", "0", "0", "0", "0" ], "steamcommunity.com": [ "steamcommunity.com", "0", "0", "0", "0", "0", "0" ], "themeforest.net": [ "themeforest.net", "0", "0", "0", "0", "0", "0" ], "anandtech.com": [ "anandtech.com", "0", "0", "1", "0", "0", "0" ], "arstechnica.com": [ "arstechnica.com", "0", "0", "0", "0", "0", "0" ], "ck101.com": [ "ck101.com", "0", "0", "0", "0", "0", "0" ], "cookpad.com": [ "cookpad.com", "0", "0", "0", "0", "0", "0" ], "css-tricks.com": [ "css-tricks.com", "0", "0", "0", "0", "0", "0" ], "doodle.com": [ "doodle.com", "0", "0", "1", "0", "0", "0" ], "dribbble.com": [ "dribbble.com", "0", "0", "1", "0", "0", "0" ], "elevenia.co.id": [ "elevenia.co.id", "0", "0", "0", "0", "0", "0" ], "espn.go.com": [ "espn.go.com", "0", "0", "0", "0", "0", "0" ], "evernote.com": [ "evernote.com", "0", "0", "0", "0", "0", "0" ], "fotostrana.ru": [ "fotostrana.ru", "0", "0", "0", "0", "0", "0" ], "h2porn.com": [ "h2porn.com", "0", "0", "0", "0", "0", "0" ], "himado.in": [ "himado.in", "0", "0", "1", "0", "0", "0" ], "interpark.com": [ "interpark.com", "0", "0", "0", "0", "0", "0" ], "io9.com": [ "io9.com", "0", "0", "1", "0", "0", "0" ], "lifehacker.com": [ "lifehacker.com", "0", "0", "1", "0", "0", "0" ], "mixi.jp": [ "mixi.jp", "0", "1", "1", "0", "0", "0" ], "nymag.com": [ "nymag.com", "0", "0", "0", "0", "0", "0" ], "searchengines.guru": [ "searchengines.guru", "0", "0", "0", "0", "0", "0" ], "serverfault.com": [ "serverfault.com", "0", "0", "0", "0", "0", "0" ], "skyrock.com": [ "skyrock.com", "0", "0", "0", "0", "0", "0" ], "sputniknews.com": [ "sputniknews.com", "0", "0", "0", "0", "0", "0" ], "statcounter.com": [ "statcounter.com", "0", "0", "0", "0", "0", "0" ], "tinypic.com": [ "tinypic.com", "0", "0", "0", "0", "0", "0" ], "twitter.com": [ "twitter.com", "0", "0", "0", "0", "0", "0" ], "vnexpress.net": [ "vnexpress.net", "0", "0", "0", "0", "0", "0" ], "watch-series-tv.to": [ "watch-series-tv.to", "0", "1", "1", "1", "-1", "0" ], "web.tv": [ "web.tv", "0", "0", "1", "0", "0", "0" ], "abcnews.go.com": [ "abcnews.go.com", "0", "0", "0", "0", "0", "0" ], "dealnews.com": [ "dealnews.com", "0", "0", "0", "0", "0", "0" ], "genius.com": [ "genius.com", "0", "0", "0", "0", "0", "0" ], "haraj.com.sa": [ "haraj.com.sa", "0", "1", "1", "0", "0", "0" ], "jugem.jp": [ "jugem.jp", "0", "1", "1", "0", "0", "0" ], "shareba.com": [ "shareba.com", "0", "0", "0", "1", "-1", "0" ], "slickdeals.net": [ "slickdeals.net", "0", "0", "0", "0", "0", "0" ], "sourceforge.net": [ "sourceforge.net", "0", "0", "0", "0", "0", "0" ], "teespring.com": [ "teespring.com", "0", "0", "0", "0", "0", "0" ], "tympanus.net": [ "tympanus.net", "0", "0", "0", "0", "0", "0" ], "weheartit.com": [ "weheartit.com", "0", "0", "0", "0", "0", "0" ], "worldoftanks.ru": [ "worldoftanks.ru", "0", "0", "0", "0", "0", "0" ], "akhbarelyom.com": [ "akhbarelyom.com", "0", "0", "0", "0", "0", "0" ], "elcomercio.pe": [ "elcomercio.pe", "0", "1", "1", "0", "0", "0" ], "faithtap.com": [ "faithtap.com", "0", "0", "0", "-1", "-1", "0" ], "pitchfork.com": [ "pitchfork.com", "0", "0", "1", "0", "0", "0" ], "suumo.jp": [ "suumo.jp", "0", "1", "1", "0", "0", "0" ], "getpocket.com": [ "getpocket.com", "0", "0", "0", "0", "0", "0" ], "say-move.org": [ "say-move.org", "0", "0", "0", "0", "0", "0" ], "tutsplus.com": [ "tutsplus.com", "0", "0", "0", "0", "0", "0" ], "www.nhs.uk": [ "www.nhs.uk", "0", "1", "1", "0", "0", "0" ], "ecnavi.jp": [ "ecnavi.jp", "0", "1", "1", "0", "0", "0" ], "unity3d.com": [ "unity3d.com", "0", "0", "1", "0", "0", "0" ], "amoory.com": [ "amoory.com", "0", "0", "0", "-1", "-1", "0" ], "weathernews.jp": [ "weathernews.jp", "0", "1", "1", "0", "0", "0" ], "wikiwiki.jp": [ "wikiwiki.jp", "0", "1", "1", "0", "0", "0" ], "giphy.com": [ "giphy.com", "0", "0", "0", "0", "0", "0" ], "myanimelist.net": [ "myanimelist.net", "0", "0", "0", "0", "0", "0" ], "huawei.com": [ "huawei.com", "0", "0", "0", "0", "0", "0" ], "taboola.com": [ "taboola.com", "0", "0", "0", "0", "0", "0" ], "udn.com": [ "udn.com", "0", "0", "0", "0", "0", "0" ], "europa.eu": [ "europa.eu", "0", "1", "1", "0", "0", "0" ], "perezhilton.com": [ "perezhilton.com", "0", "0", "0", "0", "0", "0" ], "wmaraci.com": [ "wmaraci.com", "0", "0", "0", "0", "0", "0" ], "fanpage.gr": [ "fanpage.gr", "0", "1", "1", "0", "0", "0" ], "pantip.com": [ "pantip.com", "0", "0", "0", "0", "0", "0" ], "tsite.jp": [ "tsite.jp", "0", "1", "1", "0", "0", "0" ], "auto.ru": [ "auto.ru", "0", "0", "1", "0", "0", "0" ], "vz.ru": [ "vz.ru", "0", "0", "0", "0", "0", "0" ], "hihi2.com": [ "hihi2.com", "0", "0", "0", "0", "0", "0" ], "so-net.ne.jp": [ "so-net.ne.jp", "0", "1", "1", "0", "0", "0" ], "fc2.com": [ "fc2.com", "0", "0", "0", "0", "0", "0" ], "mirtesen.ru": [ "mirtesen.ru", "0", "0", "0", "0", "0", "0" ], "livestream.com": [ "livestream.com", "0", "0", "0", "0", "0", "0" ], "all-free-download.com": [ "all-free-download.com", "0", "0", "0", "0", "0", "0" ], "ssa.gov": [ "ssa.gov", "0", "1", "1", "0", "0", "0" ], "alohatube.com": [ "alohatube.com", "0", "0", "0", "0", "0", "0" ], "kdnet.net": [ "kdnet.net", "0", "0", "0", "0", "0", "0" ], "pinterest.com": [ "pinterest.com", "0", "0", "1", "0", "0", "0" ], "bankmellat.ir": [ "bankmellat.ir", "0", "1", "1", "0", "0", "0" ], "myegy.to": [ "myegy.to", "0", "1", "1", "1", "-1", "0" ] }
    f1 = open("data_prepare/webrank/legate_processed.txt", "r")
    f2 = open("data_prepare/webrank/legate_af.txt", "a")
    # lost = open("data_prepare/phishing2/phishing_lost0.txt", "r")
    lines = f1.readlines()
    # linesLost = lost.readlines()
    for i in range(len(lines)):
        # print(lines[i])
        lines[i] = lines[i].replace('\n','').split(', ')
        changer = lost[lines[0][0]]
        print(lines[i][24])
        print(changer[1])
        lines[i][24] = changer[1]
        lines[i][25] = changer[2]
        lines[i][26] = changer[3]
        lines[i][27] = changer[4]
        lines[i][28] = changer[5]
        for j in range(len(lines[i])):
            if j>0:
                lines[i][0] += ', ' + lines[i][j]
        f2.writelines(lines[i][0] + '\n')
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
    # prepareData()
    addFeature()
    # addProtocol()
    # filterUrl()
    # filterHttps()