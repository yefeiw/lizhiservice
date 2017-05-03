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
#setup proxy
#chrome_options = webdriver.ChromeOptions()
try:
	driver = webdriver.Chrome()
	driver.get(home_url)
        #get the refs for each file
	xpath_audiolist= driver.find_element_by_xpath('//ul[contains(@class,"js-audio-list")]')
	xpath_lists = xpath_audiolist.find_elements_by_xpath('li//a[contains(@class,"audio-list-item")]')

	#find the next page button
	next_page = driver.find_elements_by_xpath('//a[contains(@class,"next")]')
	import pdb; pdb.set_trace()
	#output to file for storage for now
	with open(output_file, 'w') as f:		
		for xpath_list in xpath_lists:
			f.write (xpath_list.text)
			f.write (xpath_list.get_attribute('href' ))
		f.write('\n##########################\n')
		for xpath_next in next_page:
			f.write(xpath_next.text)
			f.write(xpath_next.get_attribute('href'))
			f.write('\n')
		f.close()
except:
		logging.error(traceback.print_exc())
finally:
	driver.close();

