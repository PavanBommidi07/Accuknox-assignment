from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender = User)
def handle_user_save(sender, instance, **kwargs):
    print("Signal triggered. Performing tasks.....")

    time.sleep(3)

    print("Task completed after waiting.")