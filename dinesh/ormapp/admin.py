from django.contrib import admin
from .models import BankLoan, BankLoanAdmin
if not admin.site.is_registered(BankLoan):
    admin.site.register(BankLoan, BankLoanAdmin)
