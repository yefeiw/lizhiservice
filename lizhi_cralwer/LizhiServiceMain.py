# error logging
import logging
import traceback

###cross file checks
import LizhiCrawler
import LizhiMail
import LizhiSoup
from selenium import webdriver

# email utilities

types = ['吐槽', '互撕', '吃喝玩乐', '嘉宾', '特别', '热点', '在美国', 'beikao default']
hosts = ['Ada', '丫头', 'Ruby', '豆包', '老王', '黑人', '奔', '阿瓜', '小哈', '小龙哥', '九月', '大白', '波波']

crawler = LizhiCrawler.LizhiCrawler(types, hosts)
soup = LizhiSoup.LizhiSoup('./email-inlined.html', './category.txt', './email-output.html')
mail = LizhiMail.LizhiMail()

output_file = "./category.txt"
try:
    driver = webdriver.PhantomJS()
    addresses = crawler.retrieve_hrefs(driver)
    crawler.process(driver, addresses)
    categories = crawler.get_categories()
    hostcount = crawler.get_hostcount()
    recentshow = crawler.get_recentshow()
    # output to file for storage for now
    with open(output_file, 'w') as f:
        for item in types:
            f.write('\n\n\ntitle#' + item + '\n')
            items = categories[item];
            f.write("total length: %d\n" % len(items))
        for person in hosts:
            f.write('host#' + person + ": \n")
            f.write("\ttotal recordings: " + str(hostcount[person]) + '\n')
            f.write("\tmost recent appearance " + recentshow[person] + '\n')
        f.close()

    soup.parse()
    mail.sendMail()


except:
    logging.error(traceback.print_exc())
finally:
    driver.close()
