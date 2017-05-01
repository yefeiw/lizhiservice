###Name: lizhi crawler
### Iteratively opens up selected list of lizhi fm posts.

### Dependencies:

#   selenium: (pip install -U selenium)
#   chrome web driver (google selenium web driver, and install accordingly)

### Tested and working


import time
import random

from selenium import webdriver

url_list = ['http://www.lizhi.fm/40624/2537307520300433414',
            'http://www.lizhi.fm/40624/2544932985626452998',
            'http://www.lizhi.fm/40624/2533934263724614150' ]
    #loop through all audio files to minimize danger of being blocked
for url in url_list:
    #setup proxy
    chrome_options = webdriver.ChromeOptions()
    #For lizhi, all web accesses are cached
    #thus we need to access via incognito to make sure each access counts as a new one.
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options=chrome_options)   
    driver.get(url)
    #click audio play button and wait for 30 seconds
    # this is to ensure that that the audio will play properly
    driver.find_element_by_class_name('play-btn').click()
    time.sleep(30+random.randint(1,30))
    #close the webpage and wait for 5 seconds for cleanup
    driver.quit()
    time.sleep(5)
 