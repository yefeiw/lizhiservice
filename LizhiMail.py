import time
import random
import json
#error logging
import logging
import traceback
#email utilities
import smtplib
import re

from email.header import Header 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
###TestData####
#html格式构造
html =  """\
<html> 
<head>Weekly Report</head> 
<body> 
<p>Hello comrades<br> 
   你们好啊<br> 
   点击进入 <a href="http://lizhi.fm/40624"> Home of our Lizhi Website</a> 
</p> 
</body> 
</html> 
"""
	    
class LizhiMail:
	def __init__(self,categories):
			self.sender = '80talkshow@gmail.com'
			self.receiver = 'jeffxanthus@gmail.com'
			self.subject = 'Beikao Weekly'
			self.data = categories
			self.content = MIMEText(html,'html')

	def sendMail(self):
	    smtpserver = 'smtp.gmail.com'
	    port=587
	    username = '80talkshow@gmail.com'
	    password = '80talkshow_1'
	    msg = MIMEMultipart('alternative')
	    msg['Subject'] = Header(self.subject,'utf-8')
	    msg.attach(self.content)
	    smtp = smtplib.SMTP(smtpserver,port)
	    smtp.starttls()
	    smtp.login(username,password)
	    smtp.sendmail(self.sender,self.receiver,msg.as_string())
	    smtp.quit()
	
	 
	# #构造图片
	#     fp = open('meinv.jpg','rb')
	#     msgImage = MIMEImage(fp.read())
	#     fp.close()
	#     msgImage.add_header('Content-ID','<meinv_image>')
	#     msg.attach(msgImage)
	 
	#构造附件
	    # att = MIMEText(open('Pictures.rar','rb').read(),'base64','utf-8')
	    # att["Content-Type"] = 'application/octet-stream'
	    # att["Content-Disposition"] = 'attatchment;filename="Pictures.rar"'
	    # msg.attach(att)
	    

