#!/usr/bin/env python
import re
import os
from datetime import datetime

logpath = os.environ['LOGPATH']

logname = "2017-04-12.log"
lookback = datetime(2017,04,12,17,47,00)

pdate = re.compile('(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})')
perror = re.compile('ERROR')
papi = re.compile('Number of UMAPI actions sent \(total, success, error\): \(\d+, \d+, (\d+)\)')
pcrit = re.compile('CRITICAL')

msgbody = ""

with open(logpath + logname, 'r') as f:
 for line in f:
 #is this line from less than 5 minutes in the past?
  m = pdate.match(line)
  if m is not None:
   lt = datetime.strptime(m.group(), "%Y-%m-%d %H:%M:%S")
   tdelta = lookback - lt
   if tdelta.seconds < 300:
    if perror.search(line): #me is not None:
     #this line contained "ERROR"
     msgbody = msgbody + line

    ma = papi.search(line)
    if ma is not None: # is not None:
     ma.group
     if int(ma.group(1)) > 0:
      print "ma: " + ma.group(1)
      #this line contained the results, and there were errors
      msgbody = msgbody + line

    if pcrit.search(line):
      msgbody = msgbody + line

if msgbody != '':
 #something wrong
 print msgbody
else:
 print "Success!"
