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
import LizhiCrawler
import LizhiMail

from selenium import webdriver
types = ['吐槽','互撕','吃喝玩乐','嘉宾','特别','热点','在美国','beikao default']

crawler = LizhiCrawler.LizhiCrawler(types)
output_file = "./category.txt"
try:
	driver = webdriver.PhantomJS()
	addresses = crawler.retrieve_hrefs(driver)
	categories = crawler.generate_categories(driver, addresses)
	#output to file for storage for now
	with open(output_file, 'w') as f:
		for item in types:
			f.write('\n\n\n'+item+'\n')
			items = categories[item];
			f.write("total length: %d\n" % len(items))
			for title in items:
				f.write(title+'\n')
		f.close()
	mail = LizhiMail.LizhiMail(output_file)
	mail.sendMail()

	
except:
	logging.error(traceback.print_exc())
finally:
	driver.close()
