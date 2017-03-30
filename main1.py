from multiprocessing import Pool
from channel_extract import channel_list
from page_parsing import get_links_from,url_list1,url_list2,item_info
import time


db_urls = [item['url'] for item in url_list1.find()]
index_urls = [item['pa_url'] for item in url_list2.find()]
x = set(db_urls)
y = set(index_urls)
rest_of_urls = x-y

def get_all_links_from(sub_channel):
    for i in range(1,101):
        if get_links_from(sub_channel,i) == -1:
            break
    time.sleep(2)

if  __name__=='__main__':
    pool=Pool()
    pool.map(get_all_links_from,list(rest_of_urls))
    pool.close()
    pool.join()