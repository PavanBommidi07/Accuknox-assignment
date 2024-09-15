import threading
from django.dispatch import Signal, receiver

test_signal = Signal()

@receiver(test_signal)
def signal_handler(sender, **kwargs):
    print(f"signal handler is running in thread: {threading.current_thread().name}")
    print(f"signal handler thread ID: {threading.get_ident()}")