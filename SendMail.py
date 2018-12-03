import smtplib
import sys
import getpass
import re    
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from email.utils import COMMASPACE, formatdate
from pathlib import Path

path = os.path.abspath( __file__ )
mypath=input("Content path  ")
print(mypath)
Emailpath= input("Email path  ")
print(Emailpath)
contents = Path(mypath).read_text()
part2 = MIMEText(contents, 'html')
with open(Emailpath, "r") as fd:
    lines = fd.read().splitlines()
email = input("email:")
password = getpass.getpass("Enter your password: ")
to = input("To:")
Subject = input("Subject:")
File = input("File:")
smtp = smtplib.SMTP('smtp.office365.com')
smtp.connect('smtp.office365.com','587')
smtp.starttls()
smtp.login(email, password)
part = MIMEBase('application', "octet-stream")
part.set_payload(open(File, "rb").read())
encoders.encode_base64(part)
encoders.encode_base64(part2)
part.add_header('Content-Disposition', 'attachment; filename=attachment.html')
msg = MIMEMultipart()
msg['Subject'] = Subject
msg['From'] = email
msg.attach(part)
msg.attach(part2);
for item in lines:
    msg['To'] = item
    smtp.sendmail(email, item, msg.as_string())
