import smtplib
from email.MIMEMultipart import *
from email.MIMEText import *

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login("","")

server.sendmail("","","thgdfhjh")

server.quit()
