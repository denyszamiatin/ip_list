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
from getIPList import getip
from sys import argv
from time import strftime
from os import path, listdir


file_name = r'iplist.' + strftime("%Y%m%d%H%M%S") + '.csv'
db_path = r'.\ipdb'
ip_db = path.join(db_path, file_name)


def _getdb():
  with open(ip_db, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for line in reader:
      print line


def _getlatestdbfile():
   return sorted(listdir(db_path))[-1]



def updatedb(ip_list):
  with open(ip_db, 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', lineterminator='\n', escapechar='|', quoting=csv.QUOTE_NONE)
    writer.writerow(['IP', 'Prefix'])
    for ip in ip_list:
      ip, pref = ip.split('/')
      writer.writerow([ip, pref])


def searchDB(ip='.'):
  with open(path.join(db_path, _getlatestdbfile()), 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader, None)
    for line in reader:
      if ip in line[0]:
        print line


# iplist = dict(reader)
#  return iplist


def main():
  url = 'http://192.168.56.102/uaix.html'
  try:
    if argv[1] == 'up':
      updatedb(getip(url)[0:10])
      searchDB()
    #      _getdb()
    else:
      print "Main"
  except IOError as er:
    print er
    # print "I/O error({0}): {1}".format(e.errno, e.strerror)


if __name__ == "__main__":
  try:
    main()
  except IndexError:
    print IndexError.errno
