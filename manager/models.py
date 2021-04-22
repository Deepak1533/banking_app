import uuid
import random

from datetime import datetime
from django.db import models


def generate_acc_num():
    return str(random.randint(100000000000, 999999999999))


class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, blank=False)
    account_number = models.CharField(max_length=10, editable=False, unique=True, default=generate_acc_num())
    account_balance = models.FloatField(blank=False, default=0.00)
    registration_time = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.account_number


class Transaction(models.Model):
    transaction_type_options = (
        ('credit', 'DEPOSIT'),
        ('debit', 'WITHDRAW'),
        ('', None)
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(blank=False, default=0.0)
    transaction_id = models.CharField(max_length=16, default=uuid.uuid4(), blank=False)
    transaction_type = models.CharField(max_length=6, choices=transaction_type_options, default=None)
    timestamp = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return self.transaction_id
