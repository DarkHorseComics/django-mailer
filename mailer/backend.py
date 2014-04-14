from django.core.mail.backends.base import BaseEmailBackend

from mailer.models import Message


class DbBackend(BaseEmailBackend):
    
    def send_messages(self, email_messages):
        db_messages = []
        for email in email_messages:
            msg = Message()
            msg.email = email
            db_messages.append(msg)
        Message.objects.bulk_create(db_messages)
        return len(db_messages)
