from gluon import *
import smtplib
def send(x,content):
	mail=smtplib.SMTP('smtp.gmail.com',25)
	mail.ehlo()
	mail.starttls()
	mail.login('knitishnitj@gmail.com','wa t.dkdja')
	mail.sendmail('knitishnitj@gmail.com',x,content)
	print("Email sent")
	mail.close()
