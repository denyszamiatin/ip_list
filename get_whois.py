# codding: utf-8

import re
import urllib2

def get_whois_domain_data_list(domain):
    url = 'https://hostmaster.ua/whois.php?domain=' + domain
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html_page = response.read()

    return re.findall(r'<td.*>(.*)<\/td><td>(.*)<\/td>', html_page)

def get_whois_ip_data_list(ip):
    url = 'https://www.colocall.net/uaix/?whois=' + ip
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html_page = response.read()

    return re.findall(r'(.*):\s+(.*)', html_page)





if __name__ == "__main__":
    list1 = get_whois_domain_data_list('lifecell.ua')

    for item in list:
        print item[0] + ':' + item[1]

    print (dir(list1))

    list = get_whois_ip_data_list('1.179.172.0')

    for item in list:
        print item[0] + ':' + item[1]

    print (dir(list2))


