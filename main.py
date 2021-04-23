import os
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "https://play.google.com/store/apps/details?id=com.covalent.kippo&hl=en_US&gl=US&showAllReviews=true"

chromebrowser = r"C:\Users\Jason\Downloads\chromedriver\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromebrowser
browser = webdriver.Chrome(chromebrowser)
browser.get(url)

#Because the site loads slowly, we need to wait 5 seconds until we can get the full page source
time.sleep(5)
html = browser.page_source
soup = BeautifulSoup(html, "lxml")

#Scroll down until you get all the reviews
SCROLL_PAUSE_TIME = 1

#Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
  #Scroll down
  browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  #Wait until finished loading more reviews
  time.sleep(SCROLL_PAUSE_TIME)

  #Calculate new scroll height and compare to last scroll height
  new_height = browser.execute_script("return document.body.scrollHeight")
  if new_height == last_height:
    break
  last_height = new_height

#Put this 2 after it has finished scraping
#browser.close()
#browser.quit()

"""

reviews_boxes = soup.find_all("div", class_="d15Mdf")
for reviews_box in reviews_boxes:
  rev_name = reviews_box.find("span", class_="X43Kjb").text
  rev_pub_date = reviews_box.find("span", class_= "p2TkOb").text
  rev_stars = int(reviews_box.find("div", class_="pf5lIe").next_element["aria-label"].split()[1]) #The element that we want doesnt have a class/id. Then from the returned string, we only take the number
  rev_likes = int(reviews_box.find("div", class_="jUL89d y92BAb").text)

  if reviews_box.find("button", class_="LkLjZd ScJHi OzU4dc"):
    #Long comment
    rev_comment = reviews_box.find("span", {"jsname":"fbQN7e"}).text
  else:
    #Short comment
    rev_comment = reviews_box.find("span", {"jsname":"bN97Pc"}).text

  print(f"Name: {rev_name}")
  print(f"Date posted: {rev_pub_date}")
  print(f"Stars: {rev_stars}")
  print(f"Likes: {rev_likes}")
  print(f"Comments: {rev_comment}")

"""