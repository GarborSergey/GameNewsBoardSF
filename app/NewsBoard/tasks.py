from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Message


def email_to_user_publication_his_message(message_id):
    message = Message.objects.get(id=message_id)
    recipient = message.sender.email

    subject = 'Your message is published in GAME-NEWS-BOARD!'
    html_content = render_to_string(
        'email_messages/message_is_public.html',
        {
            'message': message,
            'site_url': settings.SITE_URL
        }
    )

    msg = EmailMultiAlternatives(
        subject=subject,
        from_email=settings.EMAIL_FROM,
        to=[recipient]
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

