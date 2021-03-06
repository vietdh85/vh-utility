import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))
import mysql
import util

import uhyips

def main():	
	print "\n========== RUN get_stat.py ============"
	util.logNow("START AT")
	
	rcb_list = common.getRcbSites()
	for item in rcb_list:

		if item[2] == "uhyips.com":
			uhyips.run(item)
	
	common.statsRcbDaily()
	util.logNow("END AT")

############## Main #############
datetimeNow = util.getDatetimeNow()

mysql.connect()

main()

mysql.disconnect()