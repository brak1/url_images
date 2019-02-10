#!/usr/bin/env python

import urllib
import time
import os
import datetime 

months={
	1:"JAN",
	2:"FEB",
	3:"MAR",
	4:"APR",
	5:"MAY",
	6:"JUN",
	7:"JUL",
	8:"AUG",
	9:"SEP",
	10:"OCT",
	11:"NOV",
	12:"DEC"
	}

now = datetime.datetime.now()
ls_day = now.day
if ls_day < 10: 
	str_day = "0" + str(ls_day)
else:
	str_day = str(ls_day)
savedir = str_day + "-" + str(months.get(now.month))
if not os.path.exists(savedir):
	os.makedirs(savedir)
	print "Created directory: " + savedir
print savedir

while(True):
	#os.system('clear')
	timestr = time.strftime("%Y%m%d-%H%M%S")
	savefilename = "./" + savedir + "/img_" + timestr + ".jpg"
	urllib.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cheeseburger.jpg/1200px-Cheeseburger.jpg", savefilename)
	print "\n" + savefilename + " image file saved"
	time.sleep(5)



