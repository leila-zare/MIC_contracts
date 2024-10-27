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

labels = {
    "full_name":"نام و نام خانوادگی",
    "contract_type":"نوع قرارداد",
    "contract_number":"شماره قرارداد",
    "fathers_name":"نام پدر",
    "date_of_birth":"تاریخ تولد",
    "national_id":"کد ملی",
    "ID_number":"شماره شناسنامه",
    "place_of_issue":"محل صدور",
    "matiral_status":"وضعیت تاهل",
    "child_number":"تعداد فرزند",
    "military_status":"وضعیت نظام وظیفه",
    "contact_number":"شماره تماس",
    "Imail":"آدرس ایمیل",
    "refrence": "معرف",
    "postal_code":"تعداد فرزند",
    "address":"آدرس",
    "position":" سمت شغلی",
    "contract_start_date":"تاریخ شروع قرارداد",
    "contract_end_date":"تاریخ پایان قرارداد",
    "base_salary":"حقوق پایه",
    "housing_allowance":"حق مسکن",
    "food_allowance":"حق خوار و بار",
    "seniority_pay":"پایه سنوات",
    "monthly":"ماهانه",
    "child_allowance":"حق اولاد",
    "marriage_allowance":"حق تاهل",
    "transportation_allowance":"ایاب و ذهاب",
    "attraction_bonus":"فوق العاده جذب",
    "management_allowance":"حق مدیریت",
    "hourly_wage":"دستمزد ساعتی",
    "hourly_wage_with_accord":"دستمزد ساعتی با آکورد",
    "declared_salary":"حقوق ابرازی",
    "insurance_type":"نوع بیمه",
    "job_group":"گروه کاری",
    "account_number_salary":"شماره حساب حقوق",
    "IBAN_salary":"شماره شبا حقوق",
    "bank_name_salary":"نام بانک حقوق",
    "account_number_petty_cash":"شماره حساب تنخواه",
    "IBAN_petty_cash":"شماره شبا تنخواه",
    "bank_name_petty_cash":"نام بانک تنخواه",
}