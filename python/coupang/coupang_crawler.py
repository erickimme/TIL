#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import time
import csv
import random



# time stamp to check the running time
start_time = time.time()

# URL to get info
url = "http://www.coupang.com/vp/products/2801591?itemId=14692254&vendorItemId=3002041112&q=%ED%94%BC%EC%A7%80%EC%98%A4%EA%B2%94&itemsCount=36&searchId=a4f42676db164355abac4e6735dbc962&vendorItemId=3002041112&rank=1"

# bulidng webdriver instance
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get(url)

# scroll y축으로 2000 만큼 내리기
driver.execute_script("window.scrollBy(0, 2000);")
time.sleep(5)

# clicking review tab
element = driver.find_element_by_link_text('상품평')
element.click()