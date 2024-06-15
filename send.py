from email.message import EmailMessage
import mimetypes
import os
import smtplib
PASSWORD=os.getenv("webcam")  # App password from gmail
SENDER=os.getenv("Gmail")     # Gmail address
RECIEVER=os.getenv("Gmail")
def send_email(image_path):
    email_message=EmailMessage()
    email_message["Subject"]="web cam checking"
    email_message.set_content("is it doing well i think so")

    with open(image_path,"rb") as file:
        content=file.read()
    mime_type, _ = mimetypes.guess_type(image_path)
    maintype, subtype = mime_type.split('/', 1)
    email_message.add_attachment(content, maintype=maintype, subtype=subtype, filename=image_path)


    gmail=smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER,PASSWORD)
    gmail.sendmail(SENDER,RECIEVER,email_message.as_string())
    gmail.quit()
if __name__ == "__main__":
    send_email("images/21.png")

