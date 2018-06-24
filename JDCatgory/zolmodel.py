#encoding=utf8
import urllib.request
from pyquery import PyQuery as pq

import ssl
import csv
import datetime
import os
import re
context = ssl._create_unverified_context()


#file=urllib.request.urlopen('http://www.baidu.com')
file=urllib.request.urlopen('http://detail.zol.com.cn/',context=context).read()

# print ("hello")

d=pq(file)


fCat=''
sCat=''
tCat=''
cSearch=''

with open("ZOLModelKeyWords.csv","w",newline='',encoding='utf-8-sig') as csvfile: 
	writer = csv.writer(csvfile)
	writer.writerow(["类目","类目链接","型号","描述"])


	for fCat in d('#J_CategoryItems').find('.item').find('a'):
		#print("类目：",d(fCat).text(),d(fCat).attr('href'))
		clink=d(fCat).attr('href')
		try:
			file2=urllib.request.urlopen(clink,context=context).read()
			d2=pq(file2)
			for cmodellist in d2('#J_PicMode').find('H3').find('a'):
				for cmodel in d2(cmodellist):
					print(d(fCat).text(),d(fCat).attr('href'),d2(cmodel).text())
					writer.writerow([d(fCat).text(),d(fCat).attr('href'),d2(cmodel).text(),d2(cmodel).find('span').text()])
				
		except urllib.error.HTTPError as err:
			print (err.code)
			writer.writerow([d(fCat).text(),d(fCat).attr('href'),err.code])

	
print ("Good,Success!")
