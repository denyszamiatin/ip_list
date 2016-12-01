"""
getIPList.py
    Gets list of ip from https://www.colocall.net/uaix/ returns it

Usage:

"""

import urllib2
import re
import socket

# timeout in seconds
timeout = 15
socket.setdefaulttimeout(timeout)

ip_pattern = re.compile (r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}')

def getIP(site):
  req = urllib2.Request(site)
  response = urllib2.urlopen(req)
  html_page = response.read()
  iplist = ip_pattern.findall(html_page)
  return iplist

def main():
  if socket.getfqdn(socket.gethostname()).split(".")[-2] == 'astelit':
    # Proxy settings
    proxy_support = urllib2.ProxyHandler({"http": "http://proxy.astelit.ukr:3128",\
                                          "https": "http://proxy.astelit.ukr:3128"} )
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)

  url = 'https://www.colocall.net/uaix/'
  iplist = getIP(url)
  for ip in iplist:
   print ip

if __name__ == "__main__":
  main()