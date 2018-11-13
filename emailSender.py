import smtplib
from email.MIMEMultipart import *
from email.MIMEText import *

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login("omegaki113r@gmail.com","Medalofhonor@123")

server.sendmail("omegaki113r@gmail.com","chameera.kasun123@gmail.com","thgdfhjh")

server.quit()