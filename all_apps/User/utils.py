from email import message
import re
from django.core import mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string 



class EmailSend:

    @staticmethod
    def sending(data):
        subject=data['subject']
        body=data['body']
        to=data['to_email']
        context=data['context']
        html_message = render_to_string('account_activation.html', context)

        message = EmailMessage(subject=subject, body=html_message, to=to)
        message.content_subtype="html"
        message.send()

        