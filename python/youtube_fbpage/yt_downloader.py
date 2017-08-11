# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import time
import csv
import urllib
import lxml
import requests

#todo : youtube video downloading function
def yt_downloader():
    driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    driver.get(target_url)
    print("Opening Downloading link")

if __name__ == "__main__":
    # User_Input
    target_url = 'https://www.youtube.com/user/NBA/videos'
    crawled_dic = {
        'title': 'this is title',
        'video_link': "https://www.youtube.com/user/NBA/videos",
        'img_link': "https://www.naver.com",
        'play_time': "6:39",
        'hits': "12944",
        'updated_time': "2017-08-01",
    }

    # Functions
    # get_nba_posting_info(target_url)
    print(get_nba_video_info(target_url))
