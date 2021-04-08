# Writing a dictionary to a CSV file
# importing the csv module
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
import csv

def csv_file(my_dict):
    list_items = []
    # fields name
    fields = ['Name', 'Email']
    # name of csv file
    file_name = "MYFILE.csv"
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(my_dict)
    with open('MYFILE.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            list_items.append(row['Email'])
    return list_items


def email_strcuture(sender_address, sender_pass, email):
    Mail_Content = ''' HELLO '''
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
    message['To'] = email
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
    print(os.getcwd())
    return print('MAIL SENT')


sender_address = 'aritra2022@gmail.com'
sender_pass = '#'
my_dict = [{'Name': 'Aritra', 'Email' : 'caritra18@gmail.com'},
                {'Name': 'Anik', 'Email' : 'aritra.c1999@gmail.com'},
                {'Name': 'Ankita', 'Email' : 'aritra.c1999@gmail.com'}]
reciever_address = csv_file(my_dict)
for email in reciever_address:
    Mail = email_strcuture(sender_address, sender_pass, email)
    print(Mail)
