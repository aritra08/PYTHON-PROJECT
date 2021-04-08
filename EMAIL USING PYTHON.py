import os
from smtplib import SMTP
import imghdr
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import uuid

Mail_Content = ''' HELLO '''
sender_address = 'aritra2022@gmail.com'
sender_pass = '#'
reciever_address = 'caritra18@gmail.com'

message = MIMEMultipart()
pdfname = 'RESUME.pdf'
binary_pdf = open(pdfname, 'rb')
payload = MIMEBase('application', 'octate-stream', Name=pdfname)
payload.set_payload((binary_pdf).read())
encoders.encode_base64(payload)
payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
message.attach(payload)


with open('IMAGE.jpg', 'rb') as fp:
    img = MIMEImage(fp.read())
    img.add_header('Content-Disposition', 'attachment', filename="example.jpg")
    message.attach(img)


message['From'] = sender_address
message['To'] = reciever_address
message['Subject'] = 'BLOG MAIL'
body = MIMEText(Mail_Content, 'plain')
message.attach(body)
smtp_server = 'smtp.gmail.com'
smtp_port = 587
session = SMTP(smtp_server, smtp_port)
session.ehlo()
session.starttls()

session.login(sender_address, sender_pass)

session.sendmail(sender_address, reciever_address, message.as_string())
session.quit()
print('Sent Mail')
print(os.getcwd())
