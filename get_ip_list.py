# coding: utf-8
"""
getIPList.py
    Gets list of ip from https://www.colocall.net/uaix/ returns it

Usage:

"""

import urllib2
import re
import pprint

"You can use list for easy parsing: https://www.colocall.net/uaix/prefixes.txt"

IP_PATTERN = re.compile (r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}')
URL = 'https://www.colocall.net/uaix/'
PROXY = None
# urllib2.ProxyHandler({
#         "http": "http://proxy.astelit.ukr:3128",
#         "https": "http://proxy.astelit.ukr:3128"
#     })


def get_content(url):
    response = urllib2.urlopen(url)
    return response.read()


def parse_ip(text):
    return IP_PATTERN.findall(text)


def set_proxy():
    if PROXY:
        opener = urllib2.build_opener(PROXY)
        urllib2.install_opener(opener)


if __name__ == "__main__":
    set_proxy()
    pprint.pprint(parse_ip(get_content(URL)))