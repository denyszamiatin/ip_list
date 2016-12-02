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


def getip(site):
  req = urllib2.Request(site)
  response = urllib2.urlopen(req)
  html_page = response.read()
  iplist = ip_pattern.findall(html_page)
  return iplist


def main():
  url = 'http://192.168.56.102/uaix.html'
  iplist = getip(url)
  print url
  print iplist[0:10]
#   for ip in iplist:
#   print ip


if __name__ == "__main__":
  main()