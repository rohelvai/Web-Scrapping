#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: app.py
# Created: Monday, 9th March 2020 1:25:11 am
# Author: Mohammad Rohel Ahmed (mail2rohel@gmail.com)
# -----
# Last Modified: Monday, 9th March 2020 3:42:27 am
# Modified By: Mohammad Rohel Ahmed (mail2rohel@gmail.com)
# -----
# Copyright (c) 2020 xRisk
###


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import time
import sys

# URL to scrap
url = "https://www.brainyquote.com/"

#absolute path

chrome_driver_path = "/home/jack/Documents/py_practice/data_scrapping/venv/chromedriver"

chrome_options = Options()

#open chrome virtaully
chrome_options.add_argument("--headless")


webdriver = webdriver.Chrome(

    executable_path=chrome_driver_path,
    options=chrome_options
)


#default search query, no problem you can change it later
search_query = "love"

#if you want to replace search query from your terminal
if (len(sys.argv) >= 2):
    search_query = sys.argv[1]
    print(search_query)


with webdriver as driver:
    #timeout
    wait = WebDriverWait(driver, 10)

    #retrive data
    driver.get(url)
    #time.sleep()

    # find the search box
    search = driver.find_element_by_id("hmSearch")

    #press enter virtually :D
    search.send_keys(search_query + Keys.RETURN)

    #waiting time
    #time.sleep(5)

    wait.until(presence_of_element_located((By.ID, "quotesList")))
    #wait.until(presence_of_all_elements_located(By.ID, "quotesList"))

    #results
    resutls = driver.find_elements_by_class_name("m-brick")

    #closing driver
    driver.close()

    from selenium import webdriver

f = open("test.txt", "w")

url = 'https://www.brainyquote.com/'
chrome_driver_path = '/home/jack/Documents/py_practice/data_scrapping/venv/chromedriver'

chrome_options = Options()
chrome_options.add_argument('--headless')

webdriver = webdriver.Chrome(
    executable_path=chrome_driver_path, options=chrome_options
)

# default search query
search_query = "life"

if (len(sys.argv) >= 2):
  search_query = sys.argv[1]
  print(search_query)


with webdriver as driver:
    # Set timeout time
    wait = WebDriverWait(driver, 10)

    # retrive url in headless browser
    driver.get(url)

    # find search box
    search = driver.find_element_by_id("hmSearch")
    search.send_keys(search_query + Keys.RETURN)

    wait.until(presence_of_element_located((By.ID, "quotesList")))
    # time.sleep(3)
    results = driver.find_elements_by_class_name('m-brick')

    for quote in results:
      quoteArr = quote.text.split('\n')
      print(quoteArr)
      print()

    f.write(str(quoteArr) + "\n")

    # must close the driver after task finished
    driver.close()

f.close()









