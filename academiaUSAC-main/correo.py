import os
from dotenv import load_dotenv
from email.message import EmailMessage
import smtplib
import ssl

load_dotenv()

def Send(email_receiver):
    email_sender = "esgosarlavida@gmail.com"
    password = os.getenv("PASSWORD")

    subject = "Hola"
    body = "Monica"

    em = EmailMessage()
    em.set_content(body)
    em["Subject"] = subject
    em["From"] = email_sender
    em["To"] = email_receiver

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, password)
        smtp.send_message(em)


