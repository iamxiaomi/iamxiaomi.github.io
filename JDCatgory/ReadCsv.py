#encoding=utf8
import urllib.request
from pyquery import PyQuery as pq

import ssl
import csv
import datetime
import os
import re
context = ssl._create_unverified_context()


# #file=urllib.request.urlopen('http://www.baidu.com')
# file=urllib.request.urlopen('https://www.jd.com/allSort.aspx',context=context).read()

# # print ("hello")

# d=pq(file)


# fCat=''
# sCat=''
# tCat=''
# cSearch=''
brandlist=[]

with open("jdcat.csv","r",encoding="gbk") as rcsvfile: 
	readCsv = csv.reader(rcsvfile, delimiter=',') 
	#writer = csv.writer(csvfile)
	#writer.writerow(["一级类目","二级类目","三级类目","三级类目链接","类型","关键词"])
	for row in readCsv:  
		for brandkey in row[0].split():
			brandlist.append(brandkey)
			print (brandkey)
		#print(row[0].split()) 
				
	print('\n')

with open("ReadCsv.csv","w",newline='',encoding='utf-8-sig') as wcsvfile: 
	writer = csv.writer(wcsvfile)
	writer.writerow(["品牌"])
	for brandkey in brandlist:
		writer.writerow([brandkey])
	
print ("Good,Success!")
