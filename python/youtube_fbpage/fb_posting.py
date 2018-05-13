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


# opening txt/csv file that includes posting details
def import_posting_data():
    file_path = "/Users/kimeric/GitHubProjects/TIL/python/youtube_fbpage/dataset/nba/"
    csv_file_name = file_path + "%Y%m%d_%H_%M_%S"+ ".csv"

    f_csv_opened = open(file_path, 'r', encoding= 'utf-8', newline = ' ')
    reader = csv.reader(f_csv_opened)

    header = next(reader) # first row is header, use next func to start next row
    data = []
    for row in reader:
        # upload_time = []
        # upload_time = datetime.now().strftime(row[])
        # row = ['title', 'video_link', 'img_link', 'play_time', 'hits', 'updated_time']

        run_date = now_time = datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S")
        title = str(row[0])
        video_link = str(row[1])
        img_link = str(row[2])
        play_time = str(row[3])
        hits = int(row[4])
        update_time = str(row[5])

        data.append()

    print(header)
    print(data[0])



    # f_txt_opened = open("filename.txt", 'r')
    while True:
        text = f_csv_opened.readline()
        if not text:
            break
        print(text)
    f_csv_opened.close()
    return


# login fb -> fb page -> posting
def login_fb_move_to_target_url(driver, target_url, fb_id, fb_pw):
    # Build web browser with selenium.
    # Assign your path where the webdriver file located to 'executable_path' as String
    # Build bs4
    soup = BeautifulSoup(driver.page_source, 'lxml')

    # see more
    # time.sleep(5)
    # Type id & password
    type_id = driver.find_element_by_id('email').send_keys(fb_id)
    print ("Email Id entered...")
    type_pw = driver.find_element_by_id('pass').send_keys(fb_pw)
    print ("Password entered...")

    # click login button
    element = driver.find_element_by_id('loginbutton')
    element.click()

    # move to desired fbpage
    driver.get(target_url)
    print("Moving to target url")

    # write post
    post_title = "Philadelphia 76ers' Top 10 Plays Of the 2016-2017 NBA Season"
    post_url = "https://www.youtube.com/watch?v=XlGpcuaCgWI"
    post_all = post_title + '\n' + post_url

    # *todo : 여기서 부터 하면됨 로그인해서 페이지 이동해서 포스팅하면 됨
    # first click to enable posting
    driver.switch_to.alert

    pass1 = driver.find_elements_by_class_name("_5aj7")[2]
    pass1.click()

    # write something & publish
    driver.find_element_by_id('email').send_keys(fb_id)



    # by_classname = driver.find_element_by_class_name("_1hib _4bl9")
    # by_classname.click()

    # by_css = driver.find_element_by_css_selector("#js_18 > div._1j2v > div._2dck._4-u3._57d8 > div > div._ohf.rfloat > div > button > span")
    # by_css.click()
    # by_xpath = driver.find_element_by_xpath("//*[@id='js_18']/div[2]/div[3]/div/div[2]/div/button/span")
    # by_xpath.click()

    # clicking_publish = driver.find_element_by_class_name("_1mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft")
    # clicking_publish_button = driver.find_element_by_class_name("_51xa")
    # clicking_publish.click()

    # _1mf7
    # _4jy0
    # _4jy3
    # _4jy1
    # _51sy
    # selected
    # _42ft

    # post_box = driver.find_element_by_xpath(
    #     "//[@id='js_2m']/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div")
    # post_box.click()
    # post_box.send_keys(post_title)
    # post_button = driver.find_element_by_xpath("//*[text()='Publish']")
    # post_button.click()
    #
    # post_box = driver.find_element_by_xpath("//*[@button=_1mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft _42fr']/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div")
    # post_box.click()
    # # post_box.send_keys(post_title)

    # post_button = driver.find_element_by_xpath("//*[text()='Publish']")
    # post_button.click()

    return

#todo : file uploading in fb page
def yt_uploader():
    # fileInput = driver.findElement(By.name("uploadfile"));
    # fileInput.sendKeys("C:/path/to/file.jpg");
    pass


if __name__ == "__main__":

    # Credential Info
    fb_id = ""
    fb_pw = ""

    # Open Firefox
    home_url = "https://www.facebook.com/"
    page_url = "tooltooly1"
    target_url = home_url + page_url

    driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    driver.get(target_url)
    print("Opened facebook...")

    login_fb_move_to_target_url(driver, target_url, fb_id, fb_pw)