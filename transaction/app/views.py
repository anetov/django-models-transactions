from django.shortcuts import redirect, render
from .models import Customer
from .forms import TransactionForm
from django.views.generic import View
from django.db import transaction


# Create your views here.
def TransactionView(request):
    forms = TransactionForm()
    
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                sender = form.cleaned_data['sender']
                receiver = form.cleaned_data['receiver']
                amount = form.cleaned_data['amount']
                sender = Customer.objects.get(name=sender)
                sender.balance = sender.balance - int(amount)
                receiver = Customer.objects.get(name=receiver)
                receiver.balance = receiver.balance + int(amount)
                sender.save()
                receiver.save()

        return redirect('transaction')
    
    
    return render(request, 'transaction.html', {'form':form})


