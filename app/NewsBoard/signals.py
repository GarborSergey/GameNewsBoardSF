from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Message
from . import tasks


@receiver(post_save, sender=Message)
def notice_to_user_publication_his_message(sender, instance, *args, **kwargs):
    if instance.public:
        tasks.email_to_user_publication_his_message(instance.id)
    else:
        pass
