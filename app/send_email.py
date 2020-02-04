""" this file is used for sending the data through email """

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText                    
from email.mime.application import MIMEApplication
import smtplib


def send_email(email_id,password,email, height, name, average_height, count):
    
    #defining varriables
    from_email= email_id
    from_password=password
    to_email=email

    subject="Height data"
    message="Hey <strong style='color:rgb(255, 0, 0);'>%s</strong>, your height is <strong  style='color:rgb(255, 0, 0);'>%s</strong>. <br> Average height of all is <strong   style='color: rgb(55, 196, 89);'>%s</strong> and that is calculated out of <strong  style='color: rgb(55, 196, 89);'>%s</strong> people. <br> Thanks!" % (name,height, average_height, count)


    #helps to read message as html
    part1= MIMEText(message, 'html')


    msg = MIMEMultipart('mixed')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email
    
    
    #opening and reading the file
    with open ("DATA.csv",'rb') as file:
        file_data = file.read()
    

    #adding attachment
    att = MIMEApplication(file_data,_subtype="csv")
    att.add_header('Content-Disposition','attachment',filename="entries.csv")
    

    msg.attach(att)
    msg.attach(part1)

    
    #connecting to smtp server
    gmail=smtplib.SMTP_SSL('smtp.gmail.com',465)
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
