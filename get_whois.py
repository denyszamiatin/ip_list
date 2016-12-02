import re
import urllib2

def get_whois(url):
    url = 'https://hostmaster.ua/whois.php?domain=' + url
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html_page = response.read()
    r = re.findall(r'<td.*>(.*)<\/td><td>(.*)<\/td>', html_page)
    return r

list = get_whois('lifecell.ua')

for item in list:
    print item[0] + ':' + item[1]
