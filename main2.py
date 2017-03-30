from multiprocessing import Pool
from channel_extract import channel_list
from page_parsing import get_links_from,url_list1,url_list2,item_info,get_item_info
import time


db_urls = [item['item_url'] for item in url_list2.find()]
index_urls = [item['news_url'] for item in item_info.find()]
x = set(db_urls)
y = set(index_urls)
rest_of_urls = x-y

if  __name__=='__main__':
    pool=Pool()
    pool.map(get_item_info,list(rest_of_urls))
    pool.close()
    pool.join()
