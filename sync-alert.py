#!/usr/bin/env python
import re
import os
from datetime import datetime

logpath = os.environ['LOGPATH']

logname = "2017-04-12.log"
#lookback = "2017-04-12 17:46:00"
lookback = datetime(2017,04,12,17,46,00)

pdate = re.compile('(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})')
perror = re.compile('(ERROR)')
papi = re.compile('Number of UMAPI actions sent \(total, success, error\): \(\d+, \d+, (\d+)\)')


msgbody = ""

with open(logpath + logname, 'r') as f:
 for line in f:
 #is this line from less than 5 minutes in the past?
 #m = re.search("(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})", line)
  m = pdate.match(line)
  if m is not None:
   #print m.group()
   #s = m.group() + ""
   lt = datetime.strptime(m.group(), "%Y-%m-%d %H:%M:%S")
   tdelta = lookback - lt
   if tdelta.seconds < 300:
    #print "time criteria met"
    me = perror.match(line)
    if me is not None:
     #this line contained "ERROR"
     msgbody = msgbody + line + "\n"
     print "er"

    ma = papi.match(line)
    if ma is not None:
     if ma.group() > 0:
      #this line contained the results, and there were errors
      msgbody = msgbody + line + "\n"
      print "er1"

   #else:
    #print "time criteria not met"

if msgbody != '':
 #someting wong
 print msgbody
else:
 print "Success!"

