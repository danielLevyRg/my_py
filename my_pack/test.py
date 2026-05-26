#ייבוא ספריית המתנה
import time
#ייבוא ספריות של סלניום
from selenium import webdriver
from selenium.webdriver.common.by import By
import re


driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://stackoverflow.com/tags")
tags = driver.find_elements(By.CSS_SELECTOR, "a[rel=\"tag\"]")
questions = driver.find_elements(By.XPATH, "//div[@class='mt-auto d-flex jc-space-between fs-caption fc-black-400']//div[@class='flex--item']")
counter = 0
while counter <= len(tags)-1 :
   print("in " + tags[counter].text + " we have " + questions[counter].text )
   counter +=1




input("press any key to close ")