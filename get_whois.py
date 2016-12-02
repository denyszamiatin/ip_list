# codding: utf-8

import re
import urllib2

def get_whois_data_list(domain):
    url = 'https://hostmaster.ua/whois.php?domain=' + domain
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html_page = response.read()

    return re.findall(r'<td.*>(.*)<\/td><td>(.*)<\/td>', html_page)


if __name__ == "__main__":
    list = get_whois_data_list('lifecell.ua')

    for item in list:
        print item[0] + ':' + item[1]

