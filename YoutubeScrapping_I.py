from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd


# ¼¼ÆÃ
driver = webdriver.Chrome()
driver.set_window_size(800, 600)

# À¯Æ©ºê ¿­±â
Url = 'https://www.youtube.com/watch?v=pZ3DfTfQ6GM'
driver.get(Url)
time.sleep(6)

# À¯Æ©ºê ´ñ±Û ³¡±îÁö ·Îµù
last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(1.0)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height



# ÆÄ½Ì
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


str_youtube_comments = [] 
comments = soup.find_all("ytd-comment-thread-renderer", class_ = "style-scope ytd-item-section-renderer")
for comment in comments :
    comment_text = comment.find("yt-formatted-string", id="content-text").text
    try :
        str_youtube_comments.append(comment_text)
    except :
        print("Problem with emojis.")

    

# change df as Pandas
pd_data = {"Comment":str_youtube_comments}

youtube_pd = pd.DataFrame(pd_data)

youtube_pd.to_csv('C:/Users/Joohyun/Downloads/commentData6.csv', sep=',', na_rep='NaN')

