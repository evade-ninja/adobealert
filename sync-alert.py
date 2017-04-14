#!/usr/bin/env python
import re
import os
from datetime import datetime

logpath = os.environ['LOGPATH']

logname = "2017-04-12.log"
#lookback = "2017-04-12 17:46:00"
lookback = datetime(2017,04,12,17,46,00)

p = re.compile('(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})')

with open(logpath + logname, 'r') as f:
	for line in f:
		#is this line from less than 5 minutes in the past?
		#m = re.search("(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})", line)
		m = p.match(line)
		#print m.group()
		#s = m.group() + ""
		lt = datetime.strptime(m, "%Y-%m-%d %H:%M:%S")
		tdelta = lookback - lt
		if tdelta.seconds < 300:
			print "time criteria met"


#print line


