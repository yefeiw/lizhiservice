# Name: LizhiCrawler.py
# Iteratively categorize each lizhi post for Beikao and recommend what should be recorded next

# Dependencies:

#   selenium: (pip install -U selenium)
#   relevant webdriver 

import logging
import re
import time
import traceback

# home url: Homepage of Beikao
home_url = 'http://lizhi.fm/40624'
output_file = '../dump_output.txt'


# util functions


def if_xpath_exist(driver, xpath):
    test = len(driver.find_elements_by_xpath(xpath))
    if test > 0:
        return True
    else:
        return False


def get_category(title, desc, types):
    for item in types:
        if (re.search(item, title)):
            return item
        if (re.search(item, desc)):
            return item
    return "beikao default"


# class declaration reserved for future use


class LizhiStat:
    def __init__(self):
        self.title = ""
        self.description = ""
        self.viewed = 0
        self.hosts = []
        self.visitors = []


class LizhiCrawler:
    def __init__(self, types, hosts):
        self.types = types
        self.hosts = hosts
        self.categories = dict()
        self.hostcount = dict()
        self.recentshow = dict()
        return

    def add_hosts(self, desc, timestamp):
        lines = desc.text.split('\n')
        for line in lines:
            # import pdb; pdb.set_trace()
            if re.search("本期主播：", line):
                for host in self.hosts:
                    if re.search(host, line):
                        print("found host" + host + "\n")
                        if self.hostcount[host] is 0:
                            self.recentshow[host] = timestamp.text
                        self.hostcount[host] += 1

    def get_categories(self):
        return self.categories

    def get_hostcount(self):
        return self.hostcount

    def get_recentshow(self):
        return self.recentshow

    def retrieve_hrefs(self, driver):
        audio_list_addr = '//ul[contains(@class,"js-audio-list")]'
        next_page_addr = '//a[contains(@class,"next")]'
        hrefs = []
        try:

            driver.get(home_url)

            # find the next page button
            # long version for full functionality
            while if_xpath_exist(driver, audio_list_addr):
                # get the refs for each file
                xpath_audiolist = driver.find_element_by_xpath(audio_list_addr)
                xpath_lists = xpath_audiolist.find_elements_by_xpath('li//a[contains(@class,"audio-list-item")]')
                for xpath_item in xpath_lists:
                    try:
                        ref = xpath_item.get_attribute('href')
                        hrefs.append(ref)
                    except:
                        logging.error(traceback.print_exc())
                if if_xpath_exist(driver, next_page_addr):
                    # test: break anyways
                    # break
                    # mainline: go to next page
                    next_page = driver.find_element_by_xpath(next_page_addr)
                    next_page.click()
                else:
                    break

        except:
            logging.error(traceback.print_exc())
        finally:
            return hrefs

    def process(self, driver, hrefs):

        title_xpath = '//h1[contains(@class,"audioName")]'
        desc_xpath = '//div[contains(@class,"desText")]'
        timestamp_xpath = '//span[contains(@class,"audioTime")]'
        for item in self.types:
            self.categories[item] = []
        for person in self.hosts:
            self.hostcount[person] = 0
            self.recentshow[person] = ""
        try:
            for href in hrefs:
                print("href is " + href)
                driver.get(href)
                time.sleep(1)
                if (if_xpath_exist(driver, title_xpath) is False) or (if_xpath_exist(driver, desc_xpath) is False):
                    print("this href postition " + href + " is not valid, please manually verify later")
                    continue
                title = driver.find_element_by_xpath(title_xpath)
                desc = driver.find_element_by_xpath(desc_xpath)
                timestamp = driver.find_element_by_xpath(timestamp_xpath)
                # import pdb;pdb.set_trace()
                category = get_category(title.text, desc.text, self.types)
                self.add_hosts(desc, timestamp)
                self.categories[category].append(title.text)
                print(category + ": current count " + str(len(self.categories[category])))
        except:
            logging.error(traceback.print_exc())
        finally:
            pass
