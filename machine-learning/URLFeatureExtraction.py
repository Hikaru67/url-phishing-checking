# -*- coding: utf-8 -*-

# importing required packages for this section
from urllib.parse import urlparse, urlencode
import tldextract
import ipaddress
import pandas as pd
import re
import favicon

# 1.Domain of the URL (Domain) 
#scheme='https', netloc='www.google.com', path='/search', params='', query='q=hostname&sxsrf=', fragment='imgrc=b5k8yyIPXWAtPM')
def getDomain(url):
  domain = urlparse(url).netloc
  if re.match(r"^www.",domain):
    domain = domain.replace("www.","")
  return domain

# 1. Number of character '.' in URL
def numDots(url):
    try:
        return url.count('.')
    except:
        return 0

# ExtractResult(subdomain='lol1', domain='domain', suffix='com')
def subdomainLevel(url):
    try:
        subdomain = tldextract.extract(url)
        if len(subdomain):
            return subdomain.count('.') + 1
        return 0
    except:
        return 0

# 4.Finding the length of URL and categorizing (URL_Length)
def urlLength(url):
    return len(url)

# 3.Gives number of '/' in URL (URL_Depth)
def getDepth(url):
    try:
        s = urlparse(url).path.split('/')
        depth = 0
        for j in range(len(s)):
            if len(s[j]) != 0:
                depth = depth + 1
        return depth
    except:
        return 0

# 1. Number of character '-' in URL
def numDashes(url):
    try:
        return url.count('-')
    except:
        return 0

# 1. Number of character '-' in URL
def numDashesInHostname(url):
    try:
        return urlparse(url).netloc.count('-')
    except:
        return 0

# 3.Checks the presence of @ in URL (Have_At)
def haveAtSign(url):
    if "@" in url:
        at = 1
    else:
        at = 0
    return at

def haveTildeSymbol(url):
    if "~" in url:
        at = 1
    else:
        at = 0
    return at

def numUnderscore(url):
    try:
        return url.count('_')
    except:
        return 0

def numPercent(url):
    try:
        return url.count('%')
    except:
        return 0

def numQueryComponents(url):
    try:
        query = urlparse(url).query
        return query.count('&') + 1
    except:
        return 0

def numAmpersand(url):
    try:
        return url.count('&')
    except:
        return 0

def numHash(url):
    try:
        return url.count('#')
    except:
        return 0

def numNumericChars(url):
    try:
        return len(re.sub("[^0-9]", "", url))
    except:
        return 0

def noHttps(url):
    try:
        scheme = urlparse(url).scheme
        if 'https' in scheme:
            return 0
        else:
            return 1
    except:
        return 1

# 2.Checks for IP address in URL (Have_IP)
def havingIP(url):
    try:
        ipaddress.ip_address(urlparse(url).netloc)
        ip = 1
    except:
        ip = 0
    return ip

# ExtractResult(subdomain='lol1', domain='domain', suffix='com')
def domainInSubdomains(url):
    try:
        subdomain = tldextract.extract(url).subdomain
        if len(subdomain):
            if (len(tldextract.extract(url).suffix)):
                return 1
        return 0
    except:
        return 0

def domainInPaths(url):
    try:
        path = urlparse(url).path.split('/')
        for pa in path:
            if (len(tldextract.extract(url).suffix)):
                return 1
        return 0
    except:
        return 0

def httpInHostname(url):
    try:
        hostname = urlparse(url).netloc
        if 'http' in hostname:
            return 1
        return 0
    except:
        return 0

def pathLength(url):
    try:
        path = urlparse(url).path
        return len(path)
    except:
        return 0

def queryLength(url):
    try:
        query = urlparse(url).query
        return len(query)
    except:
        return 0

def doubleSlashInPath(url):
    try:
        path = urlparse(url).path
        if '//' in path:
            return 1
        return 0
    except:
        return 0

def numSensitiveWords(url):
    try:
        count = 0
        sensitiveWords = ['secure', 'account', 'webscr', 'login', 'ebayisapi', 'sign in', 'banking', 'confirm']
        for sen in sensitiveWords:
            if sen in url:
                count += 1
        return count
    except:
        return 0

# def embeddedBrandName(url):
# def pctExtHyperlinks(url):
def extFavicon(url):
    try:
        hostname = urlparse(url).netloc
        favicons = favicon.get(url)
        for favicon in favicons:
            if hostname != urlparse(favicon.url).netloc:
                return 1
        return 0
    except:
        return 0

# def insecureForms
# def relativeFormAction
# def ExtFormAction
# def AbnormalFormAction
# def PctNullSelfRedirectHyperlinks
# def FrequentDomainNameMismatch
# def FakeLinkInStatusBar

"""#### **3.1.6. Redirection "//" in URL**

Checks the presence of "//" in the URL. The existence of “//” within the URL path means that the user will be redirected to another website. The location of the “//” in URL is computed. We find that if the URL starts with “HTTP”, that means the “//” should appear in the sixth position. However, if the URL employs “HTTPS” then the “//” should appear in seventh position.

If the "//" is anywhere in the URL apart from after the protocal, thee value assigned to this feature is 1 (phishing) or else 0 (legitimate).
"""

# 6.Checking for redirection '//' in the url (Redirection)
def redirection(url):
    pos = url.rfind('//')
    if pos > 6:
        if pos > 7:
            return 1
        else:
            return 0
    else:
        return 0

# listing shortening services
shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                      r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                      r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                      r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                      r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                      r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                      r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                      r"tr\.im|link\.zip\.net"


# 8. Checking for Shortening Services in URL (Tiny_URL)
def tinyURL(url):
    match = re.search(shortening_services, url)
    if match:
        return 1
    else:
        return 0

# 9.Checking for Prefix or Suffix Separated by (-) in the Domain (Prefix/Suffix)
def prefixSuffix(url):
    if '-' in urlparse(url).netloc:
        return 1  # phishing
    else:
        return 0  # legitimate

# !pip install python-whois

# importing required packages for this section
import re
from bs4 import BeautifulSoup
import whois
import urllib
import urllib.request
from datetime import datetime

# 11.DNS Record availability (DNS_Record)
# obtained in the featureExtraction function itself


# # 12.Web traffic (Web_Traffic)
# def web_traffic(url):
#     try:
#         # Filling the whitespaces in the URL if any
#         url = urllib.parse.quote(url)
#         rank = \
#         BeautifulSoup(urllib.request.urlopen("https://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find("REACH")['RANK']
#         rank = int(rank)
#     except TypeError:
#         return 1
#     if rank > 1000000:
#         return 1
#     else:
#         return 0

# 13.Survival time of domain: The difference between termination time and creation time (Domain_Age)
def domainAge(domain_name):
    creation_date = domain_name.creation_date
    expiration_date = domain_name.expiration_date
    if (isinstance(creation_date, str) or isinstance(expiration_date, str)):
        try:
            creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        except:
            return 1
    if ((expiration_date is None) or (creation_date is None)):
        return 1
    elif ((type(expiration_date) is list) or (type(creation_date) is list)):
        return 1
    else:
        ageOfDomain = abs((expiration_date - creation_date).days)
        if ((ageOfDomain / 30) < 6):
            age = 1
        else:
            age = 0
    return age

# 14.End time of domain: The difference between termination time and current time (Domain_End)
def domainEnd(domain_name):
    expiration_date = domain_name.expiration_date
    if isinstance(expiration_date, str):
        try:
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        except:
            return 1
    if (expiration_date is None):
        return 1
    elif (type(expiration_date) is list):
        return 1
    else:
        today = datetime.now()
        end = abs((expiration_date - today).days)
        if ((end / 30) < 6):
            end = 1
        else:
            end = 0
    return end

def rankHost(url):
    try:
        # Filling the whitespaces in the URL if any
        url = urllib.parse.quote(url)
        rank = \
        xml = BeautifulSoup(urllib.request.urlopen("https://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml")
        rank = xml.find("REACH")['RANK']
        rank = int(rank)
        if rank > 1000000:
            return 1
        return 0
    except TypeError:
        return 1

def rankCountry(url):
    try:
        # Filling the whitespaces in the URL if any
        url = urllib.parse.quote(url)
        rank = \
        xml = BeautifulSoup(urllib.request.urlopen("https://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml")
        rank = xml.find("COUNTRY")['RANK']
        rank = int(rank)
        if rank > 1000000:
            return 1
        return 0
    except TypeError:
        return 1

# importing required packages for this section
import requests

# 15. IFrame Redirection (iFrame)
def iframe(response):
    if response == "":
        return 1
    else:
        if re.findall(r"(<iframe>|<frameBorder>|&lt;iframe&gt;|&lt;frameBorder&gt;)", response.text):
            return 1
        else:
            return 0

# 16.Checks the effect of mouse over on status bar (Mouse_Over)
def mouseOver(response):
    if response == "":
        return 1
    else:
        if re.findall('(onmouseover="[a-zA-Z\(\)]*"|addEventListener\("mouseover")', response.text):
            return 1
        else:
            return 0

# 17.Checks the status of the right click attribute (Right_Click)
def rightClick(response):
    if response == "":
        return 1
    else:
        if re.findall(r"event.button ?== ?2", response.text):
            return 1
        else:
            return 0

# 18.Checks the number of forwardings (Web_Forwards)
def forwarding(response):
    if response == "":
        return 1
    else:
        if len(response.history) <= 2:
            return 0
        else:
            return 1


# Function to extract features
def featureExtraction(url):
    features = []
    # Address bar based features (10)
    features.append(getDomain(url))
    
    features.append(subdomainLevel(url))
    features.append(urlLength(url))
    features.append(getDepth(url))
    features.append(haveAtSign(url))
    features.append(haveTildeSymbol(url))
    features.append(noHttps(url))
    features.append(havingIP(url))
    features.append(domainInSubdomains(url))
    features.append(domainInPaths(url))
    features.append(httpInHostname(url))
    features.append(doubleSlashInPath(url))

    features.append(numDots(url))
    features.append(numDashesInHostname(url))
    features.append(numUnderscore(url))
    features.append(numPercent(url))
    features.append(numQueryComponents(url))
    features.append(numAmpersand(url))
    features.append(numHash(url))
    features.append(numNumericChars(url))
    features.append(pathLength(url))
    features.append(queryLength(url))
    features.append(numSensitiveWords(url))

    features.append(extFavicon(url))
    features.append(redirection(url))
    features.append(tinyURL(url))
    features.append(prefixSuffix(url))

    # features.append(getDepth(url))
    # features.append(redirection(url))
    # features.append(tinyURL(url))
    # features.append(prefixSuffix(url))

    # Domain based features (4)
    dns = 0
    try:
        flags = 0
        flags = flags | whois.NICClient.WHOIS_QUICK
        domain_name = whois.whois(urlparse(url).netloc, flags=flags)
    except Exception:
        dns = 1

    features.append(dns)
    features.append(1 if dns == 1 else domainAge(domain_name))
    features.append(1 if dns == 1 else domainEnd(domain_name))
    
    features.append(rankHost(url))
    features.append(rankCountry(url))

    # HTML & Javascript based features
    try:
        response = requests.get(url, timeout=5)
    except:
        response = ""

    features.append(iframe(response))
    features.append(mouseOver(response))
    features.append(rightClick(response))
    features.append(forwarding(response))
    # print(features)

    return features



# converting the list to dataframe
feature_names = ['Domain', 'Have_IP', 'Have_At', 'URL_Length', 'URL_Depth',
                 'Redirection', 'https_Domain', 'TinyURL', 'Prefix_Suffix',
                 'DNS_Record', 'Web_Traffic', 'Domain_Age', 'Domain_End',
                 'iFrame', 'Mouse_Over', 'Right_Click', 'Web_Forwards']

def get_data():
    all_result_phishing = []

    f1 = open("data_prepare/legate2/legate_processed.txt", "r")
    lines = f1.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','').split(', ')
        for j in range(len(lines[i])):
            if j>0:
                lines[i][j] = int(lines[i][j])
    f1.close()

    f2 = open("data_prepare/phishing/phishing_processed.txt", "r")
    legates = f2.readlines()
    for i in range(len(legates)):
        legates[i] = legates[i].replace('\n','').split(', ')
        for j in range(len(legates[i])):
            if j>0:
                legates[i][j] = int(legates[i][j])
        lines.append(legates[i])
    f2.close()
    all_result_phishing = pd.DataFrame(lines)
    all_result_phishing.to_csv('data/new-processed3.csv')

    # all_result_legitimate = pd.DataFrame(lines)
    # all_result_legitimate.to_csv('data/new-processed-legate.csv')

def extract_feature(type, index):
    all_result_phishing = []
    all_result_legitimate = []

    f1 = open("data_prepare/top5000com.txt", "r")
    index = int(index)
    type = int(type)
    i = index

    lines = f1.readlines()
    while ((i-index) < 1000):
        try:
            f1 = open("data_prepare/non-phishing/legate_" + str(int(index/1000)) + ".txt", "a")
            result_phishing = featureExtraction(lines[i].replace('\n', ''))
            print(result_phishing, "i = ", i)
            result_phishing.append(type)
            all_result_phishing.append(result_phishing)
            f1.write(str(result_phishing).replace('[','').replace(']','').replace("'",'') + '\n')
            f1.close()
            i += 1
        except:
            i += 1
            pass

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='This program prints the name of my dogs'
    )
    parser.add_argument('-t', '-type')
    parser.add_argument('-i', '-index')
    
    args = parser.parse_args()  
    extract_feature(args.t, args.i)

    # get_data()
