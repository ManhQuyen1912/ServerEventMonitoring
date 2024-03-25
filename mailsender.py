import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
import time

def send(gmail,Sub, Body):
# creates SMTP session
    message = MIMEMultipart()
    message["From"] = "mail4c0d3@gmail.com"
    message["To"] = gmail
    message["Subject"] = Sub
    # message to be sent
    email_content = f"""
    {Body}
    """

    # Thêm nội dung email vào thông điệp
    message.attach(MIMEText(email_content, "plain"))
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("mail4c0d3@gmail.com", "kqfu oxxl uxvh noec")
        server.send_message(message)

send("nmquyen1912@gmail.com", "Testing", "Testing Message")