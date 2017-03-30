#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests


start_url="http://m.sohu.com/c/395/?_once_=000025_zhitongche_daohang_v3"
url_host=" http://m.sohu.com"

def get_channel_urls(url):
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    links=soup.select('a.h3Sub')
    for link in links:
        page_url=url_host+link.get('href')
        print page_url


# get_channel_urls(start_url)


channel_list='''
     http://m.sohu.com/c/32/
     http://m.sohu.com/c/57/
     http://m.sohu.com/c/53/
     http://m.sohu.com/cl/2686/
     http://m.sohu.com/c/2714/
     http://m.sohu.com/c/15/
     http://m.sohu.com/c/40/
     http://m.sohu.com/c/284/
     http://m.sohu.com/c/290/
     http://m.sohu.com/c/399/
     http://m.sohu.com/c/546/
     http://m.sohu.com/c/19/
     http://m.sohu.com/c/46/
     http://m.sohu.com/c/301/
     http://m.sohu.com/c/295/
     http://m.sohu.com/c/315/
     http://m.sohu.com/c/24/
     http://m.sohu.com/c/27/
     http://m.sohu.com/c/28/
     http://m.sohu.com/c/31/
     http://m.sohu.com/c/26/
     http://m.sohu.com/c/208/
     http://m.sohu.com/c/79/
     http://m.sohu.com/c/81/
     http://m.sohu.com/c/1918/
     http://m.sohu.com/c/1944/
     http://m.sohu.com/cl/2026/
     http://m.sohu.com/c/3445/
     http://m.sohu.com/cl/33/
     http://m.sohu.com/c/22/
     http://m.sohu.com/c/103/
     http://m.sohu.com/cl/50/
     http://m.sohu.com/cl/49/
     http://m.sohu.com/cl/29/
     http://m.sohu.com/cl/34/
     http://m.sohu.com/cl/409/
     http://m.sohu.com/cl/51/
     http://m.sohu.com/cl/134/
     http://m.sohu.com/c/16430/?v=3
     http://m.sohu.com/c/101/?v=3
     http://m.sohu.com/c/61/?v=3
     http://m.sohu.com/c/74/
     http://m.sohu.com/c/267/?v=3
     http://m.sohu.com/cl/483/
     http://m.sohu.com/cl/5124/
     http://m.sohu.com/cl/5123/
     http://m.sohu.com/cl/470/
     http://m.sohu.com/pl/586/
     http://m.sohu.com/cl/69/
     http://m.sohu.com/cl/182/
     http://m.sohu.com/cl/199/
     http://m.sohu.com/cl/70/
     http://m.sohu.com/cl/187/
     http://m.sohu.com/c/527/
     http://m.sohu.com/cl/483/
     http://m.sohu.com/cl/188/
     http://m.sohu.com/cl/189/
     http://m.sohu.com/cl/195/
     http://m.sohu.com/cl/310/
     http://m.sohu.com/cl/309/
     http://m.sohu.com/c/3124/
     http://m.sohu.com/c/3367/
     http://m.sohu.com/cl/313/
     http://m.sohu.com/cr/2543/
     http://m.sohu.com/cr/2560/
     http://m.sohu.com/cr/2561/
     http://m.sohu.com/cr/2562/
     http://m.sohu.com/cr/2563/
'''