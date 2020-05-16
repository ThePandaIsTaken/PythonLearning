from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser= webdriver.Chrome()
browser.get("https://www.instagram.com/#YourName/following/") #don't forget to enter your name
time.sleep(6)
nick = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
passwd = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
nick.send_keys("name")
passwd.send_keys("Password")
butonklik = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button/div")
butonklik.click()
time.sleep(5)
browser.get("https://www.instagram.com/p/B9_GrLanVGq/") #post link that you want to comment
time.sleep(8)
def commentagain(): #idk why i made it
    commentArea = browser.find_element_by_class_name('Ypffh')
    commentArea.click()
    commentArea = browser.find_element_by_class_name('Ypffh')
    commentArea.send_keys("hi")#Your Comment
    yorumsss = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[2]/section[3]/div/form/button")
    yorumsss.click()
    time.sleep(7)
commentagain()
