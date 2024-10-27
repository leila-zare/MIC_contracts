from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def side_barlist(request):
    return render(request , 'contracts/1.html')

def create_contract(request):
    if request.method == 'POST':
        form = forms.ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contract_list')  # صفحه‌ای که بعد از ذخیره نمایش داده می‌شود
    else:
        form = forms.ContractForm()
    return render(request, 'contracts/create_contract.html', {'form': form})