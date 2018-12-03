import smtplib
import sys
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from email.utils import COMMASPACE, formatdate
email = input("email:")
password = getpass.getpass("Enter your password: ")
to = input("To:")
Subject = input("Subject:")
File = input("File:")
smtp = smtplib.SMTP('smtp.office365.com')
smtp.connect('smtp.office365.com','587')
smtp.starttls()
part = MIMEBase('application', "octet-stream")
part.set_payload(open(File, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename=Attachment')
msg = MIMEMultipart()
msg['Subject'] = Subject
msg['From'] = email
msg['To'] = to
msg.attach(part)
smtp.login(email, password)
smtp.sendmail(email, to, msg.as_string())
