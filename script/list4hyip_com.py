import sys
import os.path
import urllib2
import re
from pyquery import PyQuery as pq

import common

def getId(url):
	arr = url.split("/")
	id = arr[len(arr) - 2]
	return id

def getSiteUrl(id, monitor, rcbUrl):
	urlRequest = "http://{0}/go/lid/{1}/".format(monitor, id)
	result = ""
	print("REQUEST: {0}".format(urlRequest))
	
	try:
		req = urllib2.urlopen(urlRequest, timeout=30)
		url = req.geturl()
	
		arr = url.split("/?")
		arr1 = arr[0].split("//")
		
		result = arr1[1].replace("www.", "")
		result = result.split("/")[0]
	except :
		print("========== ERROR ===========")
		#common.insertUnknowSite(rcbUrl, monitor)
	
	return result
	
def getRcb(monitor):
	print("list4hyip_com.getRcb()")

	rcb_url = "http://www.{0}/new/".format(monitor)
	d = pq(url=rcb_url)
	tables = d(".newstingbg .name")
	siteList = []
	
	for index, item in enumerate(tables):
		obj = {}
		obj['siteId'] = ""
		obj['id'] = getId(item.get("href"))
		
		obj['siteRCBUrl'] = "http://{0}/details/lid/{1}".format(monitor, obj['id'])
		obj['url'] = getSiteUrl(obj['id'], monitor, obj['siteRCBUrl'])
		
		if obj['url'] != '':
			siteId = common.insertSite(obj)
			obj['siteId'] = siteId
			
			siteList.append(obj)
			print("{0} - {1} - {2}".format(obj['id'], obj['url'], obj['siteId']))
				
	for item in siteList:
		common.insertSiteMonitor(item, monitor)
		
def run():
	MONITOR = "list4hyip.com"
	getRcb(MONITOR)




