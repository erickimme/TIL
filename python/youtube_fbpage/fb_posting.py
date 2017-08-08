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
        upload_time = []
        upload_time = datetime.now().strftime(row[])
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
        text = f_opened.readline()
        if not text:
            break
        print(text)
    f_opened.close()
    return


# login fb -> fb page -> posting
def login_fb_move_to_target_url(target_url, fb_id, fb_pw):
    # Build web browser with selenium.
    # Assign your path where the webdriver file located to 'executable_path' as String
    driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    driver.get(target_url)
    print ("Opened facebook...")

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

    # publish_button = driver.find_element_by_xpath("// *[ @ id = 'rc.u_0_21'] / div / div[1] / div / div[2] / div / div[1]")
    # publish_button = driver.find_element_by_xpath("//button[contains(.,'Publish')]")
    # publish_button.click()

    # frame = driver.find_element_by_xpath('//*[@id="rc.u_0_21"]/div/div[1]/div/div[2]/div/div[1]')
    # driver.switch_to.frame(frame)
    pass1 = driver.find_element_by_id("PageComposerPagelet_Admin_View")
    pass1.click()

    pass2 = driver.fi
    pass2.click()
    # write something & publish



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




if __name__ == "__main__":

    # Credential Info
    fb_id = "test@hotmail.com"
    fb_pw = "test"

    # Open Firefox
    home_url = "https://www.facebook.com/"
    page_url = "test"
    target_url = home_url + page_url

    login_fb_move_to_target_url(target_url, fb_id, fb_pw)


'''



items_len = 0
while (1):
    for i in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # waiting interval

    # Build bs4
    soup = BeautifulSoup(driver.page_source, 'lxml')
    items = soup.find_all("a", class_="_8mlbc _vbtk2 _t5r8b")
    if items_len != len(items):
        items_len = len(items)
        print("number of items: " + str(items_len))
    elif items_len == len(items):
        print("end of page")
        break
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

f = open('./dataset/instagram_jy.csv', 'w')
wr = csv.writer(f)
wr.writerow(['uid', 'datetime', 'likes', 'location', 'account', 'tags', 'comments'])
f.close()

for x in items:
    count += 1
    uid = ""
    tags = ""
    datetime = None
    likes = None
    location = None
    account = None
    comments = ""

    # URL
    target_url = x.get('href').split('?')[0]
    uid = target_url.split("/")[2]
    target_url = url + target_url
    driver.get(target_url)

    # Image
    image = x.find("div", class_="_22yr2").find("div", class_="_jjzlb").find("img").get("src")

    # Open Target Page
    soup2 = BeautifulSoup(driver.page_source, 'lxml')
    # Time
    if soup2.find("time") != None:
        datetime = soup2.find("time").get('datetime')

    # Location
    location_container = soup2.find("a", class_="_kul9p _mg7fs")
    if location_container != None:
        location = location_container.get('href').split('/')[3] + '$' + location_container.get('title').encode('utf-8')

    # Account
    if soup2.find("a", class_="_4zhc5 notranslate _jozwt") != None:
        account = soup2.find("a", class_="_4zhc5 notranslate _jozwt").get('title')

    # Tag
    tags_container = soup2.find_all("a")
    for tag in tags_container:
        if (tag.get('href') != None) and ('#' in tag.getText()):
            tags += tag.getText()

    if soup2.find("div", class_="_kkf84 _oajsw") == None:  # if nobody likes yet
        likes = 0
    else:  # caculating small number of likes
        like_container = soup2.find("div", class_="_kkf84 _oajsw").find("span", class_="_tf9x3")
        if like_container == None:
            likes = len(soup2.find("div", class_="_kkf84 _oajsw").find_all("a"))
        elif like_container.find("span") != None:
            likes = like_container.find("span").getText()
        else:  # https://www.instagram.com/p/6ZON55AFfa/
            likes = like_container.getText().encode('utf-8')[-4:-3]

    # comments
    if soup2.find("button", class_="_jpmen _8zx0v") != None:  # check if '댓글 더 보기 exists
        element = driver.find_element_by_class_name('_jpmen')
        element.click()

    comments_container = soup2.find_all("li", class_="_99ch8")
    if comments_container != None:
        for comment in comments_container:
            if comment.find("a", class_="_4zhc5 notranslate _ebg8h") != None:
                comments = comments + "<^" + comment.find("a", class_="_4zhc5 notranslate _ebg8h").get('title') + ">$"
                # indentifier(<^: account, >$: text)
                comments = comments + comment.span.getText()

    print("===={}====").format(count)
    print("uid: {}").format(uid)

    # print("url: {}").format(target_url)
    print("datetime: {}").format(datetime)
    # print("likes: {}").format(likes)
    # pprint(location)
    # print("image: {}").format(image)
    # print("account: {}").format(account)
    # print(tags)
    # print(comments)
    # print(" ")

    f = open('./dataset/instagram_jy.csv', 'a')
    wr = csv.writer(f)
    wr.writerow([uid, datetime, likes, location, account, tags.encode('utf-8'), comments.encode('utf-8')])
    f.close()
'''

'''
# -*- coding: utf-8 -*-
"""
Created on 7/19/17
Author: Jihoon Kim
"""


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
# file_path = filedialog.askopenfilename()


# print("Select your web-driver path: ")
# driver = webdriver.Chrome(file_path)
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

driver.implicitly_wait(3)

lang = int(input("Choose the language: \n 1. English \n 2. Korean\n"))

if lang == 1:
    webadr = "https://www.tripadvisor.co.uk/Attractions"
elif lang == 2:
    webadr = "https://www.tripadvisor.co.kr/Attractions"
else:
    raise ValueError("Wrong input.")

print("Type the sites you want to crawl: (type 'quit' to end)")
sites = []
while True:
    site = input()
    if site == 'quit':
        break
    sites.append(site)

for site in range(len(sites)):
    # access trip advisor page
    driver.get(webadr)

    print("========================================")
    # Test Case
    driver.find_element_by_class_name("typeahead_input").clear()
    driver.find_element_by_class_name("typeahead_input").send_keys(sites[site])
    driver.find_element_by_id("SUBMIT_THINGS_TO_DO").click()
    time.sleep(3)

    # extract last page
    print("Crawling Starts on: " + sites[site])
    soup = BeautifulSoup(driver.page_source, "html.parser")
    last_page_att = soup.find("span", {"class": "pageNum last taLnk "})
    last_page = int(last_page_att.get("data-page-number"))
    print("Number of Pages: ", last_page)

    # containers
    titles = []
    reviews = []
    ratings = []
    dates = []

    for i in range(last_page):
        print("Crawling Process: %s / %s" % (i + 1, last_page))
        # Extract Latest Review
        time.sleep(3)
        latest_review_id = driver.find_element_by_xpath("//div[@class='reviewSelector']").get_attribute("id")
        id_num = latest_review_id.split('_')[1]
        target_path_for_more_button = "#" + "review_" + id_num
        selector = target_path_for_more_button + " > div > div.ui_column.is-9 > div > div.wrap > \
        div.prw_rup.prw_reviews_text_summary_hsx > div > p > span"
        time.sleep(3)
        try:
            driver.find_element_by_css_selector(selector).click()
        except:
            pass
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        titles.extend([title.text for title in soup.find_all("span", {"class": "noQuotes"})])
        reviews.extend([review.text for review in soup.find_all("p", {"class": "partial_entry"})][2:])
        len_this_page = len([title.text for title in soup.find_all("span", {"class": "noQuotes"})])

        for num_rate in range(len_this_page):
            if lang == 2:
                ratings.append(int(soup.find_all("div", {"class": "rating reviewItemInline"})[num_rate+2].find('span')\
                                   .get("class")[1][-2:-1]))
            else:
                ratings.append(int(soup.find_all("div", {"class": "rating reviewItemInline"})[num_rate].find('span') \
                                   .get("class")[1][-2:-1]))
            dates.append(soup.find_all("span", {"class": "ratingDate relativeDate"})[num_rate].get('title'))
        if i < last_page - 1:
            driver.find_element_by_css_selector('#taplc_location_reviews_list_0 > div.prw_rup.prw_common_north_star_pagination > div > span.nav.next.taLnk').click()
        time.sleep(3)
    print("Crawling Completed: ", sites[site])
    print("========================================")
    ta_df = pd.DataFrame({'title': titles, 'review': reviews, 'rating': ratings, 'dates': dates})
    ta_df.to_csv('./data/' + sites[site] + '.csv', encoding='utf-8')
'''