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
from getIPList import _getip
from sys import argv
from time import strftime
from os import path, listdir


file_name = r'iplist.' + strftime("%Y%m%d%H%M%S") + '.csv'
db_path = r'.\ipdb'


def _getdb():
  ip_db_latest = path.join(db_path, _getlatestdbfile())
  with open(ip_db_latest, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for line in reader:
      print line


def _getlatestdbfile():
   return sorted(listdir(db_path))[-1]


def updatedb(ip_list):
  ip_db_new = path.join(db_path, r'iplist.' + strftime("%Y%m%d%H%M%S") + '.csv')
  with open(ip_db_new, 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', lineterminator='\n', escapechar='|', quoting=csv.QUOTE_NONE)
    writer.writerow(['IP', 'Prefix'])
    for ip in ip_list:
      ip, pref = ip.split('/')
      writer.writerow([ip, pref])


def searchDB(ip='.'):
  ip_db_srch = path.join(db_path, _getlatestdbfile())
  with open(ip_db_srch, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader, None)
    for line in reader:
      if ip in line[0]:
        print line


# iplist = dict(reader)
#  return iplist


if __name__ == "__main__":
  try:
    url = 'https://www.colocall.net/uaix/prefixes.txt'
    if argv[1] == 'up':
        updatedb(_getip(url)[0:10])
        searchDB()
    else:
      print "Main"
  except IOError as er:
    print "I/O error({0}): {1}".format(er.errno, er.strerror)
  except IndexError:
    print IndexError.errno
