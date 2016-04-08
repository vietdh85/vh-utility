import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

def getValues(url):
	print("getValues()")
	
	d = pq(url="https://{0}".format(url))
	list = d(".welcome-stat .col-xs-4 td")
	obj = {}
	obj['site_id'] = common.getSiteId(url)
	
	if obj['site_id'] == None:
		obj['site_id'] = -1
		
	obj['total_account'] = list[7].text_content()
	obj['active_account'] = list[11].text_content()
	obj['total_deposit'] = list[1].text_content().replace("$ ", "")
	obj['total_withdraw'] = list[3].text_content().replace("$ ", "")
	obj['time'] = long(time.time()) * 1000
	
	print("{0} - {1} - {2} {3}".format(obj['total_account'], obj['active_account'], obj['total_deposit'], obj['total_withdraw'], obj['time']))
	common.insertSiteStat(obj)

def run():	
	print "\n========== RUN coiner_biz.run() ============"
	try :
		getValues("coiner.biz")
	except Exception:
		pass
	




