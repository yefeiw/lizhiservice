###Name: LizhiCrawler.py
### Iteratively categorize each lizhi post for Beikao and recommend what should be recorded next

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
import re

###cross file checks

from selenium import webdriver
#home url: Homepage of Beikao
home_url = 'http://lizhi.fm/40624'
output_file = '../dump_output.txt'
types = ['吐槽','互撕','吃喝玩乐','嘉宾','特别','热点','在美国','beikao default']
###util functions
def if_xpath_exist(driver, xpath):
	test = len(driver.find_elements_by_xpath(xpath))
	if test > 0:
		return True
	else:
		return False

def get_category(title,desc,types):
	for item in types:
		if (re.search(item,title)):
			return item
		if (re.search(item,desc)):
			return item
	return "beikao default"

####################Structural Functions####################
class LizhiCrawler:
	def __init__(self):
		return
	def retrieve_hrefs(self,driver):
		audio_list_addr = '//ul[contains(@class,"js-audio-list")]'
		next_page_addr = '//a[contains(@class,"next")]'
		hrefs = []
		titles = []
		try:

			driver.get(home_url)
		  
			#find the next page button
			while if_xpath_exist(driver,audio_list_addr):
				 #get the refs for each file
				xpath_audiolist= driver.find_element_by_xpath(audio_list_addr)
				xpath_lists = xpath_audiolist.find_elements_by_xpath('li//a[contains(@class,"audio-list-item")]')
				for xpath_item in xpath_lists:
					try:
						ref = xpath_item.get_attribute('href')
						hrefs.append(ref)
						title = xpath_item.get_attribute('title')
						titles.append(title)
					except:
						logging.error(traceback.print_exc())
				if if_xpath_exist(driver,next_page_addr):
					next_page = driver.find_element_by_xpath(next_page_addr)
					next_page.click()
				else:
					break
				#time.sleep(1)
			
			#output to file for storage for now
			# with open(output_file, 'w') as f:		
			# 	for i in range(0,len(hrefs)):
			# 		f.write(hrefs[i])
			# 		if i < len(titles):
			# 			f.write('\t'+titles[i])
			# 		f.write('\n')
			# 	f.close()
		except:
				logging.error(traceback.print_exc())
		finally:
			return hrefs

	def generate_categories(self,driver, hrefs):
		categories = dict()
		title_xpath = ('//h1[contains(@class,"audioName")]')
		desc_xpath  =('//div[contains(@class,"desText")]')
		for item in types:
			categories[item] = []
		try:
			for href in hrefs:
				print ("href is "+href)
				driver.get(href)
				time.sleep(1)
				if not if_xpath_exist(title_xpath) or not if_xpath_exist(desc_xpath):
					print ("this href postition "+href+" is not valid, please manually verify later")
					continue
				title = driver.find_element_by_xpath(title_xpath)
				desc = driver.find_element_by_xpath(desc_xpath)
				#import pdb;pdb.set_trace()
				category = get_category(title.text,desc.text,types)
				categories[category].append(title)
				print(category+": current count " + str(len(categories[category])))
		except:
			logging.error(traceback.print_exc())
		finally:
			return categories



