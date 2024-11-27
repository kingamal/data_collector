from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import os

def send_email(email, height):
    from_email = os.getenv('GMAIL')
    from_password = os.getenv('GOOGLE_PASSWORD')
    to_email = email

    subject="Height data"
    message="Hey there, your height is <strong>%s</strong>." % height

    msg=MIMEText(message, "html")
    msg["Subjects"]=subject
    msg["To"]=to_email
    msg["From"]=from_email

    gmail=smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
