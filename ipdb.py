"""
ipdb.py
    1) Saves list of IP to csv file.
      File name: iplist%Y%m%d%H%M%S.csv
      File format:
        header('IP', 'Preix')
        rows(IP,prefix)
    2) Search ip in latest db file

Usage:

"""

import csv
from get_ip_list import get_content, parse_ip
from sys import argv
from time import strftime
from os import path, listdir


DB_PATH = r'.\ipdb'


def _get_latest_db_file():
  try:
    return sorted(listdir(DB_PATH))[-1]
  except IndexError:
    return 'DB catalog emty'


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
  if _get_latest_db_file() == 'DB catalog emty':
    print _get_latest_db_file()
    lst = ['DB catalog emty']
  elif 'iplist' in _get_latest_db_file():
    ip_db_srch = path.join(DB_PATH, _get_latest_db_file())
    with open(ip_db_srch, 'r') as csv_file:
      reader = csv.reader(csv_file, delimiter=',')
      next(reader, None)
      lst = [x[0] for x in reader if ip in x[0]]
  return lst


if __name__ == "__main__":
  try:
    if argv[1] == 'up':
 #     update_db(parse_ip(get_content('https://www.colocall.net/uaix/prefixes.txt'))[0:20])
  #    print search_in_db('2')
      print 'iplist' in _get_latest_db_file()
  except IOError as er:
    print "I/O error({0}): {1}".format(er.errno, er.strerror)
  except IndexError as er:
    print "I/O error({0}): {1}".format(er.errno, er.strerror)
