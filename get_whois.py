import re
import urllib2


def get_whois(url):
    url = 'https://hostmaster.ua/whois.php?domain=' + url
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html_page = response.read()

    r = re.findall(r'<td.*>(.*)<\/td><td>(.*)<\/td>', html_page)

    print r

    for i in r:
        print i[0] + ':' + i[1]

get_whois('lifecell.ua')
