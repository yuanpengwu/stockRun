#!/usr/bin/python

import smtplib
import os

#filename = "/home/pwu/stock/trading_result.txt"

def sendToGmail(filename):
	gmail_user = ''
	gmail_pwd = ''

	# Read a file


	sender = ''

	reciever = ''

	marker = "AUNIQUEMARKER"

	body="""
	This is a test email to send an attachment
	"""

	fo = open(filename, "r")
	lines = fo.readlines()
	for line in lines:
		print line, '\n'
		body = body + '\n' + line + '\n'
	fo.close()
  
        #print body


	#try:
	smtpObj = smtplib.SMTP('smtp.gmail.com:587')
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(gmail_user, gmail_pwd)
	smtpObj.sendmail(sender, reciever, body)
	#except Exception:
#	print "can't send email\n"
