# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class MyscrapyPipeline(object):
    def __init__(self):  
        #csv文件的位置,无需事先创建  
        #store_file = os.path.dirname(__file__) + '/spiders/qtw.csv'
        store_file="ZOLModelKeyWords123.csv"
        #打开(创建)文件  
        self.file = open(store_file,"w",newline='',encoding='utf-8-sig') 
        #csv写法  
        self.writer = csv.writer(self.file)  
        #self.writer.writerow(["类目","类目链接","型号","描述"])
          
    def process_item(self,item,spider):  
        #判断字段值不为空再写入文件  
        #if item['catName']:  
        print(99999999999999999999999999999999999999999999999999999999999999999999999999999)
        #self.writer.writerow(("123123","123123","123123","123123")) 
        self.writer.writerow((item['catName'],item['catLink'],item['modelName'],item['modelDes']))  
        return item  
      
    def close_spider(self,spider):  
        #关闭爬虫时顺便将文件保存退出  
        self.file.close() 
