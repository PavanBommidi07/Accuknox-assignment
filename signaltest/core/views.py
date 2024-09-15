import threading
from django.shortcuts import render
from django.http import HttpResponse
from .signals import test_signal

# Create your views here.

def trigger_signal(request):
    print(f"Triggering function running in thread : {threading.current_thread().name}")
    print(f"Triggering function thread ID : {threading.get_ident()}")

    test_signal.send(sender = None)

    return HttpResponse("Signal received successfully! ")
