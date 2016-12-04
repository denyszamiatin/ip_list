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
from get_ip_list import get_content, parse_ip
from sys import argv
from time import strftime
from os import path, listdir


DB_PATH = r'.\ipdb'


def _get_latest_db_file():
   return sorted(listdir(DB_PATH))[-1]


def update_db(ip_list):
  ip_db_new = path.join(DB_PATH, r'iplist.' + strftime("%Y%m%d%H%M%S") + '.csv')
  with open(ip_db_new, 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', lineterminator='\n', escapechar='|', quoting=csv.QUOTE_NONE)
    writer.writerow(['IP', 'Prefix'])
    for ip in ip_list:
      ip, pref = ip.split('/')
      writer.writerow([ip, pref])
  return ip_db_new


def search_in_db(ip='.'):
  ip_db_srch = path.join(DB_PATH, _get_latest_db_file())
  with open(ip_db_srch, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader, None)
    lst = [x[0] for x in reader if ip in x[0]]
    return lst


if __name__ == "__main__":
  try:
    url = 'https://www.colocall.net/uaix/prefixes.txt'
    if argv[1] == 'up':
      update_db(parse_ip(get_content(url))[0:20])
      print search_in_db('2')
  except IOError as er:
    print "I/O error({0}): {1}".format(er.errno, er.strerror)
  except IndexError as er:
    print "I/O error({0}): {1}".format(er.errno, er.strerror)
