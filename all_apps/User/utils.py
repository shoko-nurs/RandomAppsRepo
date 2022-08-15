from django.core.mail import EmailMessage
from django.template.loader import render_to_string 
import random 
import string


class EmailSend:

    @staticmethod
    def sending(data, template_name):
        subject=data['subject']
        body=data['body']
        to=data['to_email']
        context=data['context']
        html_message = render_to_string(template_name, context)
        # html_message = render_to_string('account_activation_reset.html', context)

        message = EmailMessage(subject=subject, body=html_message, to=to)
        message.content_subtype="html"
        message.send()



class ApiKeyGenerator:
    def claim(self, length=8):

        key = ''.join((random.choice(string.ascii_uppercase) for x in range(length)))
        return key