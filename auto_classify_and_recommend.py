###Name: lizhi crawler
### Iteratively opens up selected list of lizhi fm posts.

### Dependencies:

#   selenium: (pip install -U selenium)
#   chrome web driver (google selenium web driver, and install accordingly

import time
import random
import json
#error logging
import logging
import traceback
#email utilities
import smtplib

from selenium import webdriver
#home url: Homepage of Beikao
home_url = 'http://lizhi.fm/40624'
output_file = 'dump_output.txt'
types = ['吐槽','互撕','吃喝玩乐','嘉宾','特别','热点','在美国']
###util functions
def if_xpath_exist(driver, xpath):
	test = len(driver.find_elements_by_xpath(xpath))
	if test > 0:
		return True
	else:
		return False


#setup proxy
#chrome_options = webdriver.ChromeOptions()
try:
	hrefs = []
	titles = []
	driver = webdriver.Chrome()
	driver.get(home_url)
  
	#find the next page button
	while if_xpath_exist(driver,'//ul[contains(@class,"js-audio-list")]'):
		 #get the refs for each file
		xpath_audiolist= driver.find_element_by_xpath('//ul[contains(@class,"js-audio-list")]')
		xpath_lists = xpath_audiolist.find_elements_by_xpath('li//a[contains(@class,"audio-list-item")]')
		for xpath_item in xpath_lists:
			try:
				ref = xpath_item.get_attribute('href')
				hrefs.append(ref)
				title = xpath_item.get_attribute('title')
				titles.append(title)
			except:
				logging.error(traceback.print_exc())
		if if_xpath_exist(driver,'//a[contains(@class,"next")]'):
			next_page = driver.find_element_by_xpath('//a[contains(@class,"next")]')
			next_page.click()
		else:
			break
		#time.sleep(1)
	
	#output to file for storage for now
	with open(output_file, 'w') as f:		
		for i in range(0,len(hrefs) -1):
			f.write(hrefs[i])
			if i < len(titles):
				f.write('\t'+titles[i])
			f.write('\n')
		f.close()
except:
		logging.error(traceback.print_exc())
finally:
	driver.close();

