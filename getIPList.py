"""
getIPList.py
    Gets list of ip from https://www.colocall.net/uaix/ returns it

Usage:

"""

import urllib2
import re

url = 'http://192.168.56.102/uaix.html'

ip_pattern = re.compile (r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}')

def getIP(url):
  req = urllib2.Request(url)
  response = urllib2.urlopen(req)
  html_page = response.read()
  iplist = ip_pattern.findall(html_page)
  return iplist

def main():
  getIP(url)

if __name__ == "__main__":
  main()