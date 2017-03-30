import time
from page_parsing import url_list2

while True:
    print url_list2.find().count()
    time.sleep(5)