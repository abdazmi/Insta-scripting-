import os
from time import sleep
import wget
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

keyword = "#siamusic"

driver = webdriver.Chrome("C:\Development\chromedriver.exe")

driver.get(url="https://www.instagram.com/")
sleep(3)
username = driver.find_element_by_xpath('//input[@type="text"]')
username.clear()

username.send_keys(put your instagrm username)

password = driver.find_element_by_xpath('//input[@type="password"]')
password.clear()
password.send_keys(put your password here)

login = driver.find_element_by_xpath('//button[@type="submit"]').click()
sleep(5)
notNow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
sleep(5)
notNow2 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
sleep(5)
search = driver.find_element_by_xpath('//input[@type="text"]')
search.send_keys(keyword)
sleep(5)

search.send_keys(Keys.ENTER)
search.send_keys(Keys.ENTER)

sleep(5)
for i in range(3):
    driver.find_element_by_xpath('/html').send_keys(Keys.PAGE_DOWN)
    sleep(3)

anchers = driver.find_elements_by_tag_name("a")
anchers = [img.get_attribute('href') for img in anchers]
images = [img for img in anchers if "https://www.instagram.com/p/" in img]
# print(images)
links = []
sleep(2)

for img in images:
    sleep(2)
    driver.get(img)
    sleep(3)
    try:
        x = driver.find_element_by_xpath('//img[@class="FFVAD"]').get_attribute('src')
        links.append(x)
        print(x)

    except:
        pass

location = fr'C:\Users\Abody\Desktop\{keyword[1:]}'

# create the directory
try:
    os.mkdir(location)
except:
    pass

counter = 0
for link in links:
    save_as = location + r"\\" + keyword[1:] + str(counter) + '.jpg'
    wget.download(link, save_as)
    print("added")
    counter += 1
