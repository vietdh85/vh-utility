import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "lib")))
import util
import mysql
import hyip_scope
import hyip_tank
	
def main():	
	print "\n========== RUN get_rcb.py ============"
	util.logNow("START AT")
	
	hyip_scope.run()
	hyip_tank.run()
	
	util.logNow("END AT")

############## Main #############
datetimeNow = util.getDatetimeNow()

mysql.connect()

main()

mysql.disconnect()



