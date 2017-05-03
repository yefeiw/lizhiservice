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

crawler = LizhiCrawler.LizhiCrawler()
try:
	#driver = webdriver.Chrome()
	#addresses = crawler.retrieve_hrefs(driver)
	#categories = crawler.generate_categories(driver, addresses)
	categories = []
	mail = LizhiMail.LizhiMail(categories)
	mail.sendMail()
except:
	logging.error(traceback.print_exc())
finally:
	#driver.close()
	pass
