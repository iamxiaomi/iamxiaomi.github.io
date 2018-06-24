# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq
import csv
from myScrapy.items import zolModelItem


class GetzolmodelSpider(scrapy.Spider):
    name = 'getZolModel'
    allowed_domains = ['detail.zol.com.cn']
    start_urls = ['http://detail.zol.com.cn/']


    def parse_modelDetail(self, response):
        mItem= response.meta['item']
        print(222222222222222222225555555555)
        d2=pq(response.body)
        for cmodellist in d2('#J_PicMode').find('H3').find('a'):
            for cmodel in d2(cmodellist):
                print (d2(cmodel).text())
                mItem['modelName']=d2(cmodel).text()
                mItem['modelDes']=d2(cmodel).find('span').text() 
                yield mItem     #yield是递归迭代循环，return是立即返回跳出操作
        nextUrl=''
        print(999999999999999999999999999999999995555555555)
        print(d2('.pagebar').find('.next').attr('href'))
        if d2('.pagebar').find('.next').attr('href'):
            nextUrl='http://detail.zol.com.cn/'+d2('.pagebar').find('.next').attr('href')
            yield scrapy.Request(nextUrl,meta={'item': mItem},callback=self.parse_modelDetail)

    def parse(self, response):
        #print (1231231231231)
        #print(response.body)
        d=pq(response.body)
        # with open("modellist.csv","w",newline='',encoding='utf-8-sig') as csvfile: 
        #     writer = csv.writer(csvfile)
        #     writer.writerow(["类目","类目链接","型号","描述"])
        #     for fCat in d('#J_CategoryItems').find('.item').find('a'):
        #         mItem=zolModelItem()
        #         mItem['catName']=d(fCat).text()
        #         mItem['catLink']=d(fCat).attr('href')
        #         writer.writerow([mItem['catName'],mItem['catLink'],1,1])
        #         catLink=''
        #         catLink=d(fCat).attr('href')
        #         print (d(fCat).text(),mItem['catLink'])  

        for fCat in d('#J_CategoryItems').find('.item').find('a'):
            mItem=zolModelItem()
            mItem['catName']=d(fCat).text()
            mItem['catLink']=d(fCat).attr('href')
            catLink=''
            catLink=d(fCat).attr('href')
            #print (d(fCat).text(),mItem['catLink'])   

            yield scrapy.Request(catLink, meta={'item': mItem}, callback=self.parse_modelDetail)
