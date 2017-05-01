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
#setup proxy
#chrome_options = webdriver.ChromeOptions()
try:
	driver = webdriver.Chrome()   
	driver.get(home_url)
	#get the titles for each file
	xpath_titles = driver.find_elements_by_xpath('//div/p[contains(@class,"audioName")]')
	xpath_descriptions = driver.find_elements_by_xpath('//div[contains(@class,"audio-desc")]')
	import pdb; pdb.set_trace()
	#output to file for storage for now
	with open(output_file, 'w') as f:
		#f.write(json.dumps(xpath_titles))
		#f.write(json.dumps(xpath_descriptions))
		for xpath_title in xpath_titles:
			f.write(xpath_title.text)
			f.write('\n')	
		f.close()
except:
		logging.error(traceback.print_exc())
finally:
	driver.close();
 