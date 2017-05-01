###Name: lizhi crawler
### Iteratively opens up selected list of lizhi fm posts.

### Dependencies:

#   selenium: (pip install -U selenium)
#   chrome web driver (google selenium web driver, and install accordingly

import time
import random
import json

from selenium import webdriver
#home url: Homepage of Beikao
home_url = 'http://lizhi.fm/40624'
output_file = 'dump_output.txt'
#setup proxy
#chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome()   
driver.get(home_url)
#click audio play button and wait for 30 seconds
# this is to ensure that that the audio will play properly
xpath_titles = driver.find_elements_by_xpath('//div/p[contains(@class,"audioName")]')
xpath_descriptions = driver.find_elements_by_xpath('//div[contains(@class,"audio-desc")]')
import pdb; pdb.set_trace()
#output to file for storage for now
with open(output_file, 'w') as f:
	f.write(json.dumps(xpath_titles))
	#f.write(json.dumps(xpath_descriptions))
driver.quit()
 