from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import MyModel

@receiver(post_save, sender = MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal triggered!")

    raise Exception("Deliberate exception in signal handler")
