from bs4 import BeautifulSoup
import requests

def ceshi(url):
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    nums=len(soup.select('div.w1 > p.f > i.s'))
    print nums

ceshi('http://m.sohu.com/cl/315/?page=5000')