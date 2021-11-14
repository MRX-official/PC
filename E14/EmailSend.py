import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def Send():
    sender_email = input("Email: ")
    receiver_email = input("Receiver Email: ")
    password = input("Type your password and press enter:")

    message = MIMEMultipart("alternative")
    message["Subject"] = input("Subject: ")
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = input("Text of Email: ")

    # Turn these into plain/html MIMEText objects
    text = MIMEText(text, "plain")
    filename = input("Enter filename or path of file: ")

    # We assume that the file is in the directory where you run your Python script from
    with open(filename, "rb") as attachment:
        # The content type "application/octet-stream" means that a MIME attachment is a binary file
        part2 = MIMEBase("application", "octet-stream")
        part2.set_payload(attachment.read())

    # Encode to base64
    encoders.encode_base64(part2)

    # Add header
    part2.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(text)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
