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

nba_posting_info = {
    'title': '',
    'video_link': '',
}

nba_video_info = {
    'title': '',
    'video_link': '',
    'img_link': '',
    'play_time': '',
    'hits': '',
    'updated_time': ''
}
def get_nba_posting_info(target_url):
    '''
    get_nba_posting_info(target_url) -> dictionary type {'title1' : 't_val', 'video_link': 'v_val"}
    target_url :  youtube channel page url to crawl

    '''
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
        nba_posting_info = {
            'title': title,
            'video_link': video_link,
        }
        print(nba_posting_info)

    return nba_posting_info

def get_nba_video_info(target_url):
    # file path
    run_date = now_time = datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S")
    file_path = "/Users/kimeric/GitHubProjects/TIL/python/youtube_fbpage/dataset/nba/"
    csv_file_name = file_path + run_date + ".csv"

    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, "lxml")
    lis = soup.find_all('li', {'class': 'channels-content-item yt-shelf-grid-item'})
    count = 0

    # for header
    nba_video_info = {
        'title': '',
        'video_link': '',
        'img_link': '',
        'play_time': '',
        'hits': '',
        'updated_time': ''
    }

    with open(csv_file_name, 'w') as csv_file:
        w = csv.DictWriter(csv_file, nba_video_info.keys())
        w.writeheader()

    for li in lis:
        # count += 1
        # print("li: {}".format(li))
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
        hits_num = ''.join(x for x in hits if x.isdigit()) #get integer from string

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
            'hits': hits_num,
            'updated_time': updated_time
        }

        # print all values
        print(nba_video_info)

        # csv_file = open(csv_file_name, 'w')
        # writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        # writer.writerow(['title', 'video_link', 'img_link', 'play_time', 'hits_num', 'updated_time'])
        # crawled_dic = {
        #     'title': 'this is title',
        #     'video_link': "https://www.youtube.com/user/NBA/videos",
        #     'img_link': "https://www.naver.com",
        #     'play_time': "6:39",
        #     'hits': "12944",
        #     'updated_time': "2017-08-01",
        # }

        print("count:", count)
        with open(csv_file_name, 'a') as csv_file:
            w = csv.DictWriter(csv_file, nba_video_info.keys())
            #w.writeheader()

            #print("count:", count)
            w.writerow(nba_video_info)
            print("row number %d writerow completed" % count)
            count += 1

    print("csv file making complete...")
    return



def write_in_file():
    run_date = now_time = datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S")
    file_path = "/Users/kimeric/GitHubProjects/TIL/python/youtube_fbpage/dataset/nba/"
    txt_file_name = file_path + run_date + ".txt"
    print(txt_file_name)
    print(crawled_dic)

    f_txt = open(txt_file_name,'a')
    # f_txt.writerows(['title', 'video_link', 'img_link', 'play_time', 'hits', 'updated_time'])
    f_txt.write()

    f_txt.close
    return

def csv_maker(crawled_dic):
    run_date = now_time = datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S")
    file_path = "/Users/kimeric/GitHubProjects/TIL/python/youtube_fbpage/dataset/nba/"
    csv_file_name = file_path + run_date + ".csv"

    csv_file = open(csv_file_name, 'w')
    writer = csv.writer(csv_file)
    for key, value in crawled_dic.items():
        writer.writerow([key, value])
    csv_file.close()

    # f_csv = open(csv_file_name, 'wb')
    # writer = csv.writer(f_csv)
    # writer.writerows(['title', 'video_link', 'img_link', 'play_time', 'hits', 'updated_time'])
    # f_csv.close()
    print("csv file making complete...")
    return


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


    # write_in_file()
    # csv_maker(crawled_dic)
    # csv_maker(get_nba_video_info(target_url))



# calculating time taken
# end_time = time.time()
# running_time = end_time-start_time
# print("Total running time: {0} minutes".format(running_time / 60))
