#!/usr/bin/env python
import re
import os
from datetime import datetime

logpath = os.environ['LOGPATH']
arn = os.environ['ARN']
lookback = os.environ['LOOKBACK']


#logname = "2017-04-12.log"
#lookback = datetime(2017,04,12,17,47,00)

logname = datetime.now().strftime("%Y-%m-%d") + ".log"
t_now = datetime.now()

pdate = re.compile('(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})')
perror = re.compile('ERROR')
papi = re.compile('Number of UMAPI actions sent \(total, success, error\): \(\d+, \d+, (\d+)\)')
pcrit = re.compile('CRITICAL')

msgbody = ""

with open(logpath + logname, 'r') as f:
 for line in f:
 #is this line from less than 5 minutes in the past? (and does this line start with a timestamp?)
  m = pdate.match(line)
  if m is not None:
   lt = datetime.strptime(m.group(), "%Y-%m-%d %H:%M:%S")
   tdelta = t_now - lt
   if tdelta.seconds < int(lookback):
    if perror.search(line): #me is not None:
     #this line contained "ERROR"
     msgbody = msgbody + line

    ma = papi.search(line)
    if ma is not None: # is not None:
     ma.group
     if int(ma.group(1)) > 0:
      #this line contained the results, and there were errors
      msgbody = msgbody + line

    #are there CRITICAL messages?
    if pcrit.search(line):
      msgbody = msgbody + line

if msgbody != '':
 #something wrong
 msgbody = "Issues were detected with the Adobe Sync Tool. A summary is included below: \n\n" + msgbody
 import boto3
 client = boto3.client('sns')
 response = client.publish(TopicArn=arn,Subject="Adobe Sync Tool Alert",Message=msgbody)
 print "Issues found-SNS sent"
 #print("Response: {}".format(response))

else:
 print "No issues found!"
