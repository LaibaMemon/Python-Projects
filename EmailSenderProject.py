import smtplib                                     #its a libaray in python

to= input("Enter the Email of the Recipent:\n")

content=("Enter the content for mail:\n")

def sendEmail(to,content):
	server=smtplib.SMTP('smtp.gmail.com',587)     #its a port number for sending the email
	server.ehlo()                                 #this will try to communicate with the smtp server of the gmail
	server.starttls()
	server.login('senderemail@gmail.com','12345')
	server.sendmail('senderemail@gmail.com',to,content)
	server.close()

sendEmail(to,content)
