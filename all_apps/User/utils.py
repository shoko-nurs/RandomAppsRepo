from django.core.mail import EmailMessage

class EmailSend:

    @staticmethod
    def sending(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            to=data['to_email']

        )

        email.send()