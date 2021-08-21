import smtplib

#def send_email(customer_email):
def send_email():
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login('rdeeksharamesh@gmail.com', 'pikupiku1*')
	customer_email = 'r0000deeksha@gmail.com'
	smtpObj.sendmail('rdeeksharmesh@gmail.com', customer_email, 'Subject: Thank you for making the donation')
	smtpObj.quit()