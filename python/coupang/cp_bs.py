#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from konlpy.utils import pprint
import datetime
import time
import csv
import sys
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
import matplotlib.dates as mdates
import seaborn as sns
import dateutil
import random

# time stamp to check the running time
start_time = time.time()

# URL to get info
url = "http://www.coupang.com/vp/products/2801591?itemId=14692254&vendorItemId=3002041112&q=%ED%94%BC%EC%A7%80%EC%98%A4%EA%B2%94&itemsCount=36&searchId=a4f42676db164355abac4e6735dbc962&vendorItemId=3002041112&rank=1"

# build webdriver instance
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get(url)

# open the review tab
driver.execute_script("window.scrollBy(0, 1500);")
time.sleep(5)
element = driver.find_element_by_link_text('상품평')
element.click()

# 'lates' tab
time.sleep(5)
driver.find_elements_by_class_name('js_reviewArticleSortBtn')[1].click()
element.click()

# build bs4
soup = BeautifulSoup(driver.page_source, 'lxml')

# get the total number
item_len = int(soup.find(class_="sdp-review__average__total-star__info-count").getText().replace(',', ''))
get_len = 0
print("total: {}".format(item_len))
print("get: {}".format(get_len))

# file path
PATH = './dataset/physiogel.csv'

# initialize columns header
f = open(PATH, 'w')
wr = csv.writer(f)
wr.writerow(['uid', 'user_name', 'rating', 'date', 'text', 'option_name', 'help_count', 'perfume', 'moisture'])
f.close()   
        
while(item_len != get_len):
# paging
    page_len = len(driver.find_elements_by_class_name('js_reviewArticlePageBtn'))
    print('pages: {}'.format(page_len))
    
    for i in range(page_len):
        temp = driver.find_elements_by_class_name('js_reviewArticlePageBtn')
        temp[i].click()
        white_noise = random.random() / 5.0
        time.sleep(2.8 + white_noise)
        
        # build bs4
        soup = BeautifulSoup(driver.page_source, 'lxml')

        # get the review list
        items = soup.find(class_="js_reviewArticleListContainer").find_all("article")
        get_len += len(items)
        print("get: {}".format(get_len))

        for i in range(len(items)):
            # attributes
            uid = None
            user_name = None
            rating = None
            date = None
            text = None
            option_name = None
            help_count = None
            perfume = None
            moisture = None
            
            # uid
            try:
                uid = items[i].find(class_="js_reviewArticleHelpfulContainer").get('data-review-id').encode('utf-8')
            except:
                pass
            
            # user name
            try:
                user_name = items[i].find(class_="sdp-review__article__list__info__user__name js_reviewUserProfileImage").getText().encode('utf-8')
            except:
                pass

            # rating
            try:
                rating = int(items[i].find(class_="js_reviewArticleRatingValue").find(class_="hide_txt").get('data-rating'))
            except:
                pass

            # date
            try:
                date = items[i].find(class_="sdp-review__article__list__info__product-info__reg-date").getText().encode('utf-8')
            except:
                pass

            # text
            try:
                text = items[i].find(class_="js_reviewArticleContent").getText().encode('utf-8')
            except:
                pass

            # option_name
            try:
                option_name = items[i].find(class_="sdp-review__article__list__info__product-info__name").getText().encode('utf-8')
            except:
                pass

            # help_count
            try:
                help_count = int(items[i].find(class_="js_reviewArticleHelpfulContainer").get('data-count'))
            except:
                pass

            # perfume
            try:
                perfume = items[i].find("span", string=u"향 만족도").parent.find_all("span")[1].getText().encode('utf-8')
            except:
                pass

            # moisture
            try:
                moisture = items[i].find("span", string=u"보습력").parent.find_all("span")[1].getText().encode('utf-8')
            except:
                pass

            print("=={}".format((get_len - 5) + i) + "==") 
            print(uid)
            print(user_name)
            print(date)
            print(rating)
            print(text)
            print(option_name)
            print("help_count: {}".format(help_count))
            print(perfume)
            print(moisture)
            print(" ")

            # write a record
            f = open(PATH, 'a')
            wr = csv.writer(f)
            wr.writerow([uid, user_name, rating, date, text, option_name, help_count, perfume, moisture])
            f.close()
    
    # move to next 10 pages
    try:
        driver.find_element_by_class_name('js_reviewArticlePageNextBtn').click()
        white_noise = random.random() / 5.0
        time.sleep(2.8 + white_noise)
    except:
        pass
   
print(" ")

end_time = time.time()
running_time = end_time - start_time
print("Total running time: {} minutes").format(running_time / 60)