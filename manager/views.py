from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.mail import send_mail

from .models import User
from .forms import UserForm, TransactionForm


class IndexView(View):

    def get(self, request):

        users = User.objects.all()
        context = {
            "users": users
        }

        return render(request, 'manager/index.html', context=context)


class AddUserView(View):

    def get(self, request):
        form = UserForm()
        context = {
            'user_form': form,
            'message': ''
        }

        return render(request, 'manager/add_user.html', context=context)

    def post(self, request):
        form = UserForm(request.POST)
        message = ""
        if form.is_valid():
            message = "User Added Successfully!"
            form.save()

        context = {
            'user_form': form,
            "message": message
        }

        return render(request, 'manager/add_user.html', context=context)


class AddTranscationView(View):

    def get(self, request,):
        form = TransactionForm()

        context = {
            'trans_form': form,
            'message': ''
        }

        return render(request, 'manager/add_transaction.html', context=context)

    def post(self, request):
        data = request.POST

        form = TransactionForm(data)
        user_id = data["user"][0]
        user = User.objects.filter(id=user_id).first()

        message = ""
        if form.is_valid() and data["transaction_type"] != "None":
            mes = ""
            if data["transaction_type"] == "credit":
                user.account_balance += float(data["amount"])
                mes = f"Your account {user.account_number} is credited by amount {data['amount']}. " \
                      f"Current Balance is {user.account_balance}"
            elif data["transaction_type"] == "debit":
                user.account_balance -= float(data["amount"])
                mes = f"Your account {user.account_number} is debited by amount {data['amount']}. " \
                      f"Current Balance is {user.account_balance}"

            form.save()
            user.save()

            print(mes)

            send_mail(
                'Transaction Update',
                message,
                'bank.manager@skc.com',
                [user.email],
                fail_silently=True,
            )

            form = TransactionForm()
            message = "Transaction Added Successfully!"

        context = {
            'trans_form': form,
            "message": message
        }

        return render(request, 'manager/add_transaction.html', context=context)
