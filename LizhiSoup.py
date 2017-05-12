###Name: LizhiSoup.py
### Automatic Modifies the email HTML before sending it

### Dependencies:

#   bs4: (pip install bs4)
from bs4 import BeautifulSoup
#error logging
import logging
import traceback
#deepcopy utils
import copy
#search for added markups
import re


class LizhiSoup:
	def __init__(self,in_file, in_element, out_file):
		self.in_file = in_file
		self.in_element = in_element
		self.out_file = out_file
	def parse(self):
		try:
			#Special notice: need to specify html parser to suppress all possible warnings
			instance = BeautifulSoup(open(self.in_file),"html.parser")
			text = instance.find('td',id='to_be_replaced')
			text_replacement = instance.find('p',id='example_css')
			with open(self.in_element,"r") as f:
				lines = f.readlines()
				for line in lines:
					line = line.replace('\n','')
					if(len(line) is 0 or line =="\n"):
						continue
					#create new tag
					#text_replacement.string = line
					if re.search("title",line):
						new_line = instance.new_tag('h3')
						text_replacement.append(new_line)
						new_line.string = line.split('#')[1]
						new_line.style = instance.find('p',id='example_css').style
					elif re.search("host",line):
						new_line = instance.new_tag('h3')
						text_replacement.append(new_line)
						new_line.string = line.split('#')[1]
						new_line.style = instance.find('p',id='example_css').style
					else:
						new_line = instance.new_tag('p')
						text_replacement.append(new_line)
						new_line.string = line
						new_line.style = instance.find('p',id='example_css').style
				f.close()
			with open(self.out_file, "w") as file:
				file.write(str(instance))
				file.close()
		except:
			logging.error(traceback.print_exc())
		finally:
			pass

if __name__ =='__main__':
	test_object = LizhiSoup('./email-inlined.html','./category.txt','./email-output.html')
	test_object.parse()

