#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: arushimadan
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

url = "https://sensortower.com/ios/US/barclays-services-limited/app/barclays/536248734/review-history?selected_tab=reviews"
#result = requests.get(url)
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get(url)
i=1
for n in range(1,33):
    element = driver.find_element_by_class_name('pagination-input')
    element.clear()
    element.send_keys(str(n))
    element.send_keys(u'\ue007')
    time.sleep(2)
    src = driver.page_source
    soup = BeautifulSoup(src, features="lxml")
#    print(soup)
    for k in soup.findAll('div', attrs={'class': 'break-wrap-review'}):
        review = k.find('span')
        print(review.text)
        print("Review End*************")
        f = open(str(i).zfill(2)+'.txt', 'w')
        i+=1
        f.write(review.text)
        f.close()

