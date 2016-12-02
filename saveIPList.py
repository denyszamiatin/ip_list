"""
saveIPList.py
    saves list of IP to csv file.
    File name: iplist_date_time.csv
    File format:
    header('IP', 'Preix')
    rows(IP,prefix)

Usage:

"""

import csv
from getIPList import getIP
from sys import argv, exc_info
from time import strftime

file_time = strftime("%Y%m%d_%H%M%S")
ip_db = r'.\ipdb\iplist' + file_time + '.csv'


def updateDB(ip_list):
  with open(ip_db, 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', lineterminator='\n', escapechar='|', quoting=csv.QUOTE_NONE)
    writer.writerow(['IP', 'Prefix'])
    for ip in ip_list:
      ip, pref = ip.split('/')
      writer.writerow([ip, pref])


def getDB():
  with open(ip_db, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for line in reader:
      print line


# iplist = dict(reader)
#  return iplist


def main():
  url = 'http://192.168.56.102/uaix.html'
  try:
    if argv[1] == 'up':
      updateDB(getIP(url)[0:10])
      getDB()
    else:
      print "Main"
  except IOError as e:
    print e
    # print "I/O error({0}): {1}".format(e.errno, e.strerror)


if __name__ == "__main__":
  try:
    main()
  except IndexError:
    print IndexError.errno
