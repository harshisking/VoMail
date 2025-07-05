import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
load_dotenv()



def sender(to_email, body):
    #loading the env
    EMAIL= os.getenv("EMAIL_ADDRESS")
    PASSWORD= os.getenv("EMAIL_PASSWORD")
    
    msg = MIMEText(body,"plain")
    msg["Subject"] = 'Test Message from VoMail Sender'
    msg["From"]=EMAIL
    msg["To"]=to_email

    #starting the server
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL,PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email Sent")
    except Exception as e:
        print("ERROR:",e)

def main():
    load_dotenv()
    email = os.getenv('EMAIL_ADDRESS')
    sender('vomail@test.com', "Hi test Email from VoMail Sender")


if __name__=='__main__':
    main()