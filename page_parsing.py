# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import demjson
import pymongo
import re
import httplib
import random
from channel_extract import channel_list

client=pymongo.MongoClient('localhost',27017)
ceshi=client['ceshi']
url_list1=ceshi['url_list1']
url_list2=ceshi['url_list2']
item_info=ceshi['item_info']

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.113 Safari/537.36',
    'Connection':'keep-alive'
}

# proxy_list=[
#     'http://218.7.170.190:3128',
#     'http://124.65.80.242:8080',
#     'http://119.38.160.59:80',
#     'http://218.241.153.22:80',
#     'http://220.181.163.129:80',
# ]
# proxy_ip=random.choice(proxy_list)
# proxies={'http':proxy_ip}


url_host="http://m.sohu.com"

#spider1,爬取新闻URL
def get_sub_channel(channel):
    try:
        wb_data=requests.get(channel,headers=headers)
        if wb_data.status_code == 200:
            soup=BeautifulSoup(wb_data.text,'lxml')
            url=""
            if soup.find('nav',{'class':'site'}):
                sub_channels=soup.select('nav.site > a')
                for sub_channel_url in sub_channels:
                    url=url_host+sub_channel_url.get('href')
                    if len(url) < 30:
                        url_list1.insert_one({'url':url})
                        print url
            else:
                url=channel
                url_list1.insert_one({'url': url})
                print url
        else:
            pass
    except requests.RequestException:
        pass


def get_links_from(sub_channel,page=1):
    sub_channel_url=sub_channel+'?page='+str(page)
    try:
        wb_data=requests.get(sub_channel_url,headers=headers)
        if wb_data.status_code == 200:
            time.sleep(1)
            soup=BeautifulSoup(wb_data.text,'lxml')
            #是否达到最后一页
            if page > 1 and len(soup.select('div.w1 > p.f > i.s')) < 2:
                return -1
            links=soup.select('section > div.it > a')
            for link in links:
                flag=link.get('href')
                if flag:
                    if re.match(r'/n/\d+/',flag):
                        item_url=url_host+flag
                        url_list2.insert_one({'item_url':item_url,'pa_url':sub_channel})
                        print item_url
        else:
            pass
    except requests.RequestException:
        pass
# for c in channel_list.split():
#     get_sub_channel(c)

# ln=get_sub_channel('http://m.sohu.com/c/32/')
# for i in ln:
#     get_links_from(i)

def get_item_info(url):
    time.sleep(1)
    try:
        wb_data=requests.get(url,headers=headers)
        if wb_data.status_code == 200:
            soup=BeautifulSoup(wb_data.text,'lxml')
            news_url=url
            title=soup.title.text.split('-')[0] if len(soup.title.text.split('-')) > 0 else None
            cate=soup.title.text.split('-')[1]  if len(soup.title.text.split('-')) > 1 else None
            news_from=list(soup.select('div.article-info')[0].stripped_strings)[0] if soup.find_all('div','article-info') and len(list(soup.select('div.article-info')[0].stripped_strings)) > 0 else None
            date=list(soup.select('div.article-info')[0].stripped_strings)[1] if soup.find_all('div','article-info') and len(list(soup.select('div.article-info')[0].stripped_strings)) > 1 else None
            content=""
            if soup.find("p",'para'):
                for para in soup.select("p.para"):
                    content+=para.get_text()
                    content+='\n'
            else:
                pass
            #异步加载情况
            if soup.find('div',{'id':'rest_content'}):
                rest_get_url = url_host + "/api/n/v3/rest/" + url.split('/')[-2]+'/'
                try:
                    rest_data=requests.get(rest_get_url,headers=headers)
                    if rest_data.status_code == 200:
                        json2py=demjson.decode(rest_data.text)
                        rest_content=json2py[u'rest_content']
                        soup2=BeautifulSoup(rest_content,'lxml')
                        for para in soup2.select("p.para"):
                            content+=para.get_text()
                            content+='\n'
                except requests.RequestException:
                    pass

            editor=soup.select('div.editor')[0].get_text() if soup.find_all('div','editor') else None
            # print 'title: ', title
            # print 'editor: ', editor
            # print 'news_url: ', news_url
            # print 'news_from: ', news_from
            # print 'date: ', date
            # print 'cate: ', cate
            # print 'content: ', content
            try:
                print content
            except UnicodeEncodeError:
                pass
            print '-------------------- '
            item_info.insert_one({'title':title,'cate':cate,'news_url':news_url,'news_from':news_from,'content':content,'editor':editor})
        else:
            pass
    except requests.RequestException:
        pass
# def get_all_links():
#     for i in channel_list.split():
#         get_sub_channel(i)
#     for item in url_list1.find():
#         get_links_from(item['url'])
#
#
# for c in channel_list.split():
#     get_sub_channel(c)

# for i in channel_list.split():
#     get_sub_channel(i)

# get_item_info('http://m.sohu.com/n/341861687/')
