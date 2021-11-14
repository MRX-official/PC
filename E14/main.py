import EmailSend
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#Made by Alejandro Cavazos Valdés

def main():
    EmailSend.Send()

if __name__ == "__main__":
    main()
