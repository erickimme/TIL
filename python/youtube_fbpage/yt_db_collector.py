# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import time
import csv
import urllib
import lxml
import requests

# check start time to calculate running time
# start_time = time.time()

nba_video_info = {
    'title': '',
    'video_link': '',
    'img_link': '',
    'play_time': '',
    'hits': '',
    'updated_time': ''
}

def get_nba_video_link(target_url):
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, "lxml")
    lis = soup.find_all('li', {'class': 'channels-content-item yt-shelf-grid-item'})
    for li in lis:
        title = li.find('a', {'title': True})['title']
        video_link = 'https://www.youtube.com' + li.find('a', {'href': True})['href']
        """title, videolink
        <a class="yt-uix-sessionlink yt-uix-tile-link  spf-link  yt-ui-ellipsis yt-ui-ellipsis-2" 
        dir="ltr" title="Cleveland Cavaliers' Top 25 Plays of the 2016-2017 NBA Season" 
        aria-describedby="description-id-568300"
        data-sessionlink="ei=im6BWaOMOceAqQHl-r2oDA&feature=c4-videos-u&ved=CDgQlx4iEwij-f3H87fVAhVHQCoKHWV9D8Uomxw"
        href="/watch?v=4dcH7cajFFg">
        "Cleveland Cavaliers' Top 25 Plays of the 2016-2017 NBA Season"
        </a> 
        """
        img_link = li.find('img', {'src': True})['src']
        '''img
        <img aria-hidden="true" 
        width="196" 
        alt onload=";window.__ytRIL && __ytRIL(this)" 
        data-ytimg="1"
        src="https://i.ytimg.com/vi/4dcH7cajFFg/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLD7xJlecR1bz1IiSS7UsOHApBuQNg"
        >
        '''

        # play_time = li.find('span', {'class' : 'video-time-overlay video-time-overlay-default'}).text
        play_time = li.find('span', {'class': 'video-time'}).text
        '''play time
        <span class="video-time-overlay video-time-overlay-default" aria-hidden="true">
        <span aria-label="6 minutes, 38 seconds">6:38</span></span>
        '''

        hits = li.find_all('li')[2].text
        updated_time = li.find_all('li')[3].text
        '''hits & updated_time
        <ul class="yt-lockup-meta-info">
            <li>56,516 views></li>
            <li>12 hours ago</li>
        </ul>
        hits_and_updated_time = li.find('ul',{'class': 'yt-lockup-meta-info'})
        '''

        nba_video_info = {
            'title': title,
            'video_link': video_link,
            'img_link': img_link,
            'play_time': play_time,
            'hits': hits,
            'updated_time': updated_time
        }
        # print all values
        print(nba_video_info)

        # print title and video link
        # print(nba_video_info['title'])
        # print(nba_video_info['video_link'])
        # print("title: %s, video_link: $s" % (str(nba_video_info['title']), str(nba_video_info['video_link'])))
        # print("title: {0}, video_link: {1}".format(nba_video_info['title'], nba_video_info['video_link'])
    return nba_video_info

def write_in_file(sample_dic):
    run_date = now_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    file_path = "/Users/kimeric/GitHubProjects/TIL/python/youtube_fbpage/dataset/"
    txt_file_name = file_path + run_date + ".txt"
    print(txt_file_name)
    print(sample_dic)

    # f_txt = open("/Users/kimeric/GitHubProjects/TIL/python/FastCampus_CSschool/FC_CSS_practice/dataset/accountBook.txt",
    #              'a')
    # f_txt.writerow(['title', 'video_link', 'img_link', 'play_time', 'hits', 'updated_time'])
    # f_txt.write()

    # f_txt.close
    return

# sample_dic = {
#                 'title' : 'this is title',
#                 'video_link' : "https://www.youtube.com/user/NBA/videos",
#                 'img_link' : "https://www.naver.com",
#                 'play_time' : "6:39",
#                 'hits' : "12944",
#                 'updated_time' : "2017-08-01",
#             }
#
# write_in_file(sample_dic)


if __name__ == "__main__":
    target_url = 'https://www.youtube.com/user/NBA/videos'
    get_nba_video_link(target_url)
    # print(nba_video_info.items())






'''
# initialize url addresses to crawl
home_url = "https://www.youtube.com/"
target_url = "user/NBA/videos" # target page url
open_url = "https://www.youtube.com/user/NBA/videos" # attatch the remaining address to open
image = "" # image source url
count = 0
print(open_url)

# Build web browser with selenium.
# Assign your path where the webdriver file located to 'executable_path' as String
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get(open_url)

# Build bs4
soup = BeautifulSoup(driver.page_source, 'lxml')
'''



# calculating time taken
# end_time = time.time()
# running_time = end_time-start_time
# print("Total running time: {0} minutes".format(running_time / 60))
