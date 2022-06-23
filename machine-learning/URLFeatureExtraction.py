# -*- coding: utf-8 -*-

# importing required packages for this section
from urllib.parse import urlparse, urlencode
import tldextract
import ipaddress
import pandas as pd
import re
import favicon

# Domain of the URL (Domain) 
#scheme='https', netloc='www.google.com', path='/search', params='', query='q=hostname&sxsrf=', fragment='imgrc=b5k8yyIPXWAtPM')
def getDomain(url):
  domain = urlparse(url).netloc
  if re.match(r"^www.",domain):
    domain = domain.replace("www.","")
  return domain

def domainLength(url):
    return len(urlparse(url).netloc)

# 1. Number of character '.' in URL
def numDots(url):
    try:
        return url.count('.')
    except:
        return 0

# ExtractResult(subdomain='lol1', domain='domain', suffix='com')
def subdomainLevel(url):
    try:
        subdomain = tldextract.extract(url).subdomain
        if len(subdomain):
            return subdomain.count('.') + 1
        return 0
    except:
        return 0

# Finding the length of URL and categorizing (URL_Length)
def urlLength(url):
    return len(url)

# Gives number of '/' in URL (URL_Depth)
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

# Number of character '-' in URL
def numDashes(url):
    try:
        return url.count('-')
    except:
        return 0

# Number of character '-' in URL
def numDashesInHostname(url):
    try:
        return urlparse(url).netloc.count('-')
    except:
        return 0

# Checks the presence of @ in URL (Have_At)
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
        if len(query):
            return query.count('&') + 1
        return 0
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

# Checks for IP address in URL (Have_IP)
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
            if (len(tldextract.extract(subdomain).suffix)):
                return 1
        return 0
    except:
        return 0

def domainInPaths(url):
    try:
        path = urlparse(url).path.split('/')
        for pa in path:
            if (len(tldextract.extract(pa).suffix)):
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

# Checking for redirection '//' in the url (Redirection)
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


# Checking for Shortening Services in URL (Tiny_URL)
def tinyURL(url):
    match = re.search(shortening_services, url)
    if match:
        return 1
    else:
        return 0

# Checking for Prefix or Suffix Separated by (-) in the Domain (Prefix/Suffix)
def prefixSuffix(url):
    if '-' in urlparse(url).netloc:
        return 1  # phishing
    else:
        return 0  # legitimate


# importing required packages for this section
import re
from bs4 import BeautifulSoup
import whois
import urllib
import urllib.request
from datetime import datetime


# Survival time of domain: The difference between termination time and creation time (Domain_Age)
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

# End time of domain: The difference between termination time and current time (Domain_End)
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
        return -1

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
        return -1

# importing required packages for this section
import requests

# IFrame Redirection (iFrame)
def iframe(response):
    if response == "":
        return 1
    else:
        if re.findall(r"(<iframe>|<frameBorder>|&lt;iframe&gt;|&lt;frameBorder&gt;)", response.text):
            return 1
        else:
            return 0

# Checks the effect of mouse over on status bar (Mouse_Over)
def mouseOver(response):
    if response == "":
        return 1
    else:
        if re.findall('(onmouseover="[a-zA-Z\(\)]*"|addEventListener\("mouseover")', response.text):
            return 1
        else:
            return 0

# Checks the status of the right click attribute (Right_Click)
def rightClick(response):
    if response == "":
        return 1
    else:
        if re.findall(r"event.button ?== ?2", response.text):
            return 1
        else:
            return 0

# Checks the number of forwardings (Web_Forwards)
def forwarding(response):
    if response == "":
        return 1
    else:
        if len(response.history) <= 2:
            return 0
        else:
            return 1

def featureExtraction2(url):
    features = []
    # Address bar based features (10)
    features.append(getDomain(url))
    features.append(subdomainLevel(url))
    features.append(numQueryComponents(url))
    features.append(domainInSubdomains(url))
    features.append(domainInPaths(url))
    return features

def featureExtractionLost(url):
    features = []
    # Address bar based features (10)
    features.append(getDomain(url))
    features.append(urlLength(url))
    features.append(getDepth(url))
    features.append(pathLength(url))
    features.append(queryLength(url))
    return features

# Function to extract features
def featureExtraction(url):
    features = []
    # Address bar based features (10)
    features.append(getDomain(url))

    features.append(domainLength(url))# 1
    features.append(subdomainLevel(url))
    # features.append(urlLength(url))
    # features.append(getDepth(url))
    features.append(haveAtSign(url))
    features.append(haveTildeSymbol(url))
    features.append(noHttps(url))# 5
    features.append(havingIP(url))
    features.append(domainInSubdomains(url))
    features.append(domainInPaths(url))# 8
    features.append(httpInHostname(url))
    features.append(doubleSlashInPath(url))

    features.append(numDots(url))# 11
    features.append(numDashesInHostname(url))
    features.append(numUnderscore(url))
    features.append(numPercent(url))
    features.append(numQueryComponents(url))# 15
    features.append(numAmpersand(url))
    features.append(numHash(url))
    features.append(numNumericChars(url))
    # features.append(pathLength(url))
    # features.append(queryLength(url))
    features.append(numSensitiveWords(url))

    features.append(extFavicon(url))#20
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
    features.append(1 if dns == 1 else domainAge(domain_name))# 25
    features.append(1 if dns == 1 else domainEnd(domain_name))
    
    features.append(rankHost(url))
    features.append(rankCountry(url))

    # HTML & Javascript based features
    try:
        response = requests.get(url, timeout=5)
    except:
        response = ""

    features.append(iframe(response))# 30
    features.append(mouseOver(response))
    features.append(rightClick(response))
    features.append(forwarding(response))
    # print(features)

    return features



# converting the list to dataframe
feature_names = [
    'Domain',
    'Domain_Length',
    'Subdomain_Level',
    'Url_Length',
    'Url_Depth',
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
    'Path_Length',
    'Query_Length',
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

def extractFeaturePhishing(type, index, limit = 8000):
    all_result_phishing = []
    all_result_legitimate = []

    f1 = open("data_prepare/phishing2/verified_online.txt", "r")
    index = int(index)
    type = int(type)
    i = index
    index = int(index/limit) * limit

    lines = f1.readlines()
    while ((i-index) < limit):
        try:
            f1 = open("data_prepare/phishing2/phishing_lost" + str(int(index/limit)) + ".txt", "a")
            result_phishing = featureExtraction2(lines[i].replace('\n', ''))
            print(result_phishing, "i = ", i)
            result_phishing.append(type)
            all_result_phishing.append(result_phishing)
            f1.write(str(result_phishing).replace('[','').replace(']','').replace("'",'') + '\n')
            f1.close()
            i += 1
        except:
            i += 1
            pass

def extractFeatureLegate(type, index, limit = 1000):
    all_result_phishing = []
    all_result_legitimate = []

    f1 = open("data_prepare/webrank/des2.txt", "r")
    index = int(index)
    type = int(type)
    i = index
    index = int(index/limit) * limit

    lines = f1.readlines()
    while ((i-index) < limit):
        try:
            f1 = open("data_prepare/webrank/legate_" + str(int(index/limit)) + ".txt", "a")
            result_phishing = featureExtraction(lines[i].replace('\n', ''))
            print(result_phishing, "i = ", i)
            result_phishing.append(type)
            all_result_phishing.append(result_phishing)
            f1.write(str(result_phishing).replace('[','').replace(']','').replace("'",'') + '\n')
            f1.close()
            i += 1
        except:
            print('ext')
            i += 1
            pass

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='This program extract features of url'
    )
    parser.add_argument('-t', '-type')
    parser.add_argument('-i', '-index')
    
    args = parser.parse_args()
    if int(args.t) == 1:
        extractFeaturePhishing(args.t, args.i)
    else:
        extractFeatureLegate(args.t, args.i)

    # get_data()
