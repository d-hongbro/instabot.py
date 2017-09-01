import sys
import os
import logging
import requests
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def send_mail(in_subject, in_content):
    server = smtplib.SMTP('smtp.mail.yahoo.com', 465)
    server.starttls()
    server.login(os.environ['EMAIL_LOGIN'], os.environ['EMAIL_PASSWORD'])    
    for address in os.environ['EMAIL_SEND_TO']: 
        msg = MIMEMultipart()
        msg['From'] = os.environ['EMAIL_LOGIN'] 
        msg['To'] = address
        msg['Subject'] = in_subject
 
        msg.attach(MIMEText(in_content, 'plain'))
 
        text = msg.as_string()
        server.sendmail(os.environ['EMAIL_LOGIN'], address, text)
    server.quit()


if __name__ == '__main__':
    send_mail(sys.argv[1], sys.argv[2])

