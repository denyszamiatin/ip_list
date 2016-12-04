"""
getIPList.py
    Gets list of ip from https://www.colocall.net/uaix/ returns it

Usage:

"""

import urllib2
import re
import socket
# import pprint

# timeout in seconds
timeout = 5
socket.setdefaulttimeout(timeout)

URL = 'http://192.168.56.102/uaix.html'
IP_PATTERN = re.compile (r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}')
PROXY = None
# urllib2.ProxyHandler({
#         "http": "http://proxy.astelit.ukr:3128",
#         "https": "http://proxy.astelit.ukr:3128"
#     })


def _getip(site):
  req = urllib2.Request(site)
  response = urllib2.urlopen(req)
  html_page = response.read()
  iplst = IP_PATTERN.findall(html_page)
  return iplst


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
  # pprint.pprint(parse_ip(get_content(URL)))
  iplist = _getip(URL)
  print URL
  print iplist[0:10]
