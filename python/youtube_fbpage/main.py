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

from youtube_fbpage import get_nba_video_link


# Create video list from Youtube channel
target_url = 'https://www.youtube.com/user/NBA/videos'
get_nba_video_link(target_url)

# Login & Direct to FB page


#
