import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from django.conf import settings

class Email:
    @staticmethod
    def sendSignUpConfirmation(request, to_username, to_user_email):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Account successfully created!!!"
        msg["From"] = ""