from django import forms
from .models import Customer

class TransactionForm(forms.Form):
    sender = forms.CharField( max_length=100)
    receiver = forms.CharField(max_length=100)
    amount = forms.CharField(max_length=100)