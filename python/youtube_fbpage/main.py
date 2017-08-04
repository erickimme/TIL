# -*- coding: utf-8 -*-

# Import Modules
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import time
import csv
import urllib
import lxml
import requests

# self-built modules
from yt_db_collector import get_nba_video_link
from fb_posting import import_posting_data, login_fb_move_to_target_url



# Create video list from Youtube channel
target_url = 'https://www.youtube.com/user/NBA/videos'
get_nba_video_link(target_url)

# Login & Direct to FB page

# open txt file to read upload info

# copy "posting detail (title, link)

#

# * TODO : more to come
# 1) youtube 에서 콘텐츠 선별 (카테고리별 인기동영상 분류 및 각 영상 링크 포함된 자료 수집)
# 2) 분류된 콘텐츠별 페이스북 페이지로 자동 업로드
# 3) 페이스북 자동 공유
# 4)

