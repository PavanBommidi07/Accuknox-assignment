from django.test import TestCase
from django.db import transaction
from .models import MyModel

# Create your tests here.

class SignalTransactionTestCase(TestCase):

    def test_signal_transaction(self):
        try:
            with transaction.atomic():
                obj = MyModel(name = "Test Name")
                obj.save()
        except Exception as e:
            print(f"Excecution caught: {e}")

        self.assertEqual(MyModel.objects.count(), 0)
