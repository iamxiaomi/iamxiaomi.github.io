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
file=urllib.request.urlopen('https://www.jd.com/allSort.aspx',context=context).read()

# print ("hello")

d=pq(file)


fCat=''
sCat=''
tCat=''
cSearch=''

with open("JDCategoryKeyWords.csv","w",newline='',encoding='utf-8-sig') as csvfile: 
	writer = csv.writer(csvfile)
	writer.writerow(["一级类目","二级类目","三级类目","三级类目链接","类型","关键词"])


	for fCat in d('.category-item'):
		print("一级类目：",d(fCat).find('.item-title').find('span').text())
		fCatText=d(fCat).find('.item-title').find('span').text()

		for sCat in d(fCat).find('.items').find('.clearfix'):
			print("二级类目：",d(sCat).find('dt').text())
			sCatText=d(sCat).find('dt').text()

			for tCat in d(sCat).find('dd').find('a'):
				cslink='https:'+d(tCat).attr('href')
				print("三级类目：",d(tCat).text(),cslink)
				tCatText=d(tCat).text()
				tCatLink='https:'+d(tCat).attr('href')

				try:
					file2=urllib.request.urlopen(cslink,context=context).read()
					d2=pq(file2)
					for cSearch in d2('.J_selectorLine'):
						print("类型：",d2(cSearch).find('.sl-wrap').find('span').text())
						print("关键词：",d2(cSearch).find('.sl-value').find('.J_valueList').find('li').text())
						csType=d2(cSearch).find('.sl-wrap').find('span').text()
						csKeyWords=d2(cSearch).find('.sl-value').find('.J_valueList').find('li').text()

						writer.writerow([fCatText,sCatText,tCatText,tCatLink,csType,csKeyWords])
				except urllib.error.HTTPError as err:
						csType=err.code
						csKeyWords=err.code
						print (err.code)
						writer.writerow([fCatText,sCatText,tCatText,tCatLink,csType,csKeyWords])
				
		print('\n')

	
print ("Good,Success!")
