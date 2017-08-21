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
	def __init__(self):
			recipient_list = '../hosts.txt'
			self.sender = '80talkshow@gmail.com'
			self.receiver = []
			with open(recipient_list,'r') as f:
				lines = f.readlines()
				for line in lines:
					self.receiver.append(line)
			self.subject = 'Beikao Weekly'
			self.attachment = ""


	def sendMail(self):
		profile_input = '../profile.txt'
		with open(profile_input,'r') as f:
			lines = f.readlines()
			username = lines[0]
			password = lines[1]
			smtp = yagmail.SMTP(username,password)
			smtp.send(to=self.receiver,subject=self.subject,contents = ['./email-output.html',self.attachment])


####unit test
if __name__ =='__main__':
	mail = LizhiMail()
	mail.sendMail()