from django.forms import ModelForm

from .models import User, Transaction


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'account_balance']


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['user', 'amount', 'transaction_type']
