import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))
import mysql
import util

import unitiro_com
import webflipfunds_com
import custommining_com
import unitedswissbanks_com
import stockmarketinv_club
import fxprofit_biz
import managerhourly_com
import nanoproinvest_com
import bitcoinnetworks_biz

def main():	
	print "\n========== RUN get_stat.py ============"
	util.logNow("START AT")
	
	unitiro_com.run()
	webflipfunds_com.run()
	custommining_com.run()
	unitedswissbanks_com.run()
	stockmarketinv_club.run()
	fxprofit_biz.run()
	managerhourly_com.run()
	nanoproinvest_com.run()
	bitcoinnetworks_biz.run()
	
	util.logNow("END AT")

############## Main #############
datetimeNow = util.getDatetimeNow()

mysql.connect()

main()

mysql.disconnect()



