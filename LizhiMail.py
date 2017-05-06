###Name: LizhiMail.py
### Automatic Send mails with formatted HTMLs and attachments

### Dependencies:

#   yagmail: (pip install yagmail)

import time
import random
import json
#error logging
import logging
import traceback
#email utilities
import yagmail
import re

	    
class LizhiMail:
	def __init__(self,attachment):
			self.sender = '80talkshow@gmail.com'
			self.receiver = 'jeffxanthus@gmail.com'
			self.subject = 'Beikao Weekly'
			self.attachment = attachment


	def sendMail(self):
	    username = '80talkshow@gmail.com'
	    password = '80talkshow_1'
	    smtp = yagmail.SMTP(username,password)
	    smtp.send(to=self.receiver,subject=self.subject,contents = ['./email-output.html',self.attachment])


####unit test
mail = LizhiMail('category.txt')
mail.sendMail()