import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "lib")))
import util
import mysql
import hyipdollar_com
	
def main():	
	print "\n========== RUN test_get_rcb.py ============"
	util.logNow("START AT")
	
	hyipdollar_com.run()
	
	util.logNow("END AT")

############## Main #############
datetimeNow = util.getDatetimeNow()

mysql.connect()

main()

mysql.disconnect()



