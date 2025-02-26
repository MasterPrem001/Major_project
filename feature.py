from urllib.parse import urlparse,urlencode
import ipaddress
import re
import pandas as pd
#checking if the entered url is a valid url
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
#using features used in making of the model in features.ipynb,converting url into features list with 0 and 1
def havingip(url):
    try:
        ipaddress.ip_address(url)
        ip = 1
    except:
        ip = 0
    return ip

def haveAt(url):
    if "@" in url:
        at = 1
    else:
        at = 0
    return at

def getlength (url):
    if len(url) > 50:
        length = 1
    else:
        length = 0
    return length

def getdepth(url):
    d = urlparse(url).path.split('/')
    depth = 0
    for j in range (len(d)):
        if len(d[j])!= 0:
            depth = depth+1
    return depth

def redirect (url):
    pos = url.rfind("//")
    if pos > 5:
        if pos >6:
            return 1
        else:
            return 0
    else:
        return 0
    
def httpDomain(url):
  domain = urlparse(url).netloc
  if 'https' in domain:
    return 1
  else:
    return 0

shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                      r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                      r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                      r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                      r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                      r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                      r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                      r"tr\.im|link\.zip\.net"

def short (url):
    match = re.search(shortening_services,url)
    if match:
        return 1
    else:
        return 0
    
def prefix(url):
    if '-' in urlparse(url).netloc:  
        return 1
    else:
        return 0

#making a list and apprending it with 1 and 0 results using above functions
def feature(url, label):
    if not is_valid_url(url):
        raise ValueError("Invalid URL")
    
    features = []
    features.append(havingip(url))
    features.append(haveAt(url))
    features.append(getlength(url))
    features.append(getdepth(url))
    features.append(redirect(url))
    features.append(httpDomain(url))
    features.append(short(url))
    features.append(prefix(url))
    features.append(label)
    return features
