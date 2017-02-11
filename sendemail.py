import smtplib
from_addr = ''
to_addr = ''
message = """From: {} <{}>
To: {} <{}> 
Subject: {}
{}
"""
from_name="";
msg="test message";
subject="test subject"
to_name="";

message_to_send = message.format(from_name, from_addr, to_name,to_addr, subject, msg)
# Credentials (if needed)
username = from_addr
password = ''
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 