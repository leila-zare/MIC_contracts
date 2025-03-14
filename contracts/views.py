
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import ContractForm
from django.contrib import messages
from .models import Contract
from django.db.models import Q
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.forms.models import model_to_dict


def home_sidebar(request):
    return render(request , 'contracts/sidebarlist.html')

def contract_list(request):
    contracts_table_2 = Contract.objects.all()  # دریافت تمام قراردادها
    field_lables = {field.name:field.verbose_name for field in Contract._meta.get_fields() if field.concrete}  # استخراج نام فیلدها
    
    
    query = request.GET.get('q','')
    contracts_table_1 = Contract.objects.all()
    if query: 
        contracts_table_1 = contracts_table_1.filter(full_name = query)
        contracts_table_1 = contracts_table_1[:4]

    # contracts_table_2 = Contract.objects.all()    
    selected_fields_1 = [ "full_name","national_id", "date_of_birth","contact_number",
                            "contract_type", "contract_number","bank_name_salary","IBAN_salary"]
    field_lables_selected_1 = {field.name:field.verbose_name for field in Contract._meta.get_fields() if field.name in selected_fields_1}



    return render(request, 'contracts/contract_list.html', {
                                                            'contracts_table_1': contracts_table_1,
                                                            'contracts_table_2': contracts_table_2,
                                                            'field_lables': field_lables,
                                                            'field_lables_selected_1':field_lables_selected_1,
                                                            'query': query})
def create_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.data)
            messages.success(request, "قرارداد با موفقیت ثبت شد")
            return redirect('contracts:create_contract')  # صفحه‌ای که بعد از ذخیره نمایش داده می‌شود
        # else:
        #     messages.error(request, "اطلاعات ثبت نشد، لطفا دویاره تلاش کنید")
        #     return redirect('contracts:create_contract')
    elif request.method == "GET":
        # messages.error(request, "اطلاعات ثبت نشد، لطفا دویاره تلاش کنید")
        # print(form.errors)
        form = ContractForm(request.POST)
    return render(request, 'contracts/create_contracts.html', {'form': form})

def delete_contract(request, contract_id):
    # if request.method == "POST":
        record = get_object_or_404(Contract, pk = contract_id)
        record.delete()
        return redirect("contracts:contractlist")
    
# اصلاح فرم
def edit_contract(request, contract_id):
    # گرفتن رکورد از دیتابیس
    contract = get_object_or_404(Contract, id=contract_id)
   
    if request.method == 'POST':
        # اگر درخواست POST بود، داده‌های جدید را پردازش کن
        print(request.POST)
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()  # ذخیره تغییرات در دیتابیس
            # messages.success(request, "قرارداد با موفقیت ویرایش شد")
            return redirect('contracts:contractlist')  # بازگشت به صفحه لیست قراردادها
    else:
        # اگر درخواست GET بود، فرم را با داده‌های رکورد پر کن
        form = ContractForm(instance=contract)

    return render(request, 'contracts/edit_contract.html', {'form': form , 'contract': contract}) 

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
# import weasyprint

# برای تست اینکه میخوام از داده های دستابیس استفاده کنم

def generate_pdf(request, contract_id):
    contract = Contract.objects.get(id=contract_id)  
    return render(request, 'contracts/generate_pdf.html', {'contract': contract})

    




def success_view(request):
    return render(request, 'contracts/sidebarlist.html')

     
# def personnel_view(request):
#     return render(request, 'contracts/personel.html')

def personnel_view(request):
    contracts_table_2 = Contract.objects.all()  # دریافت تمام قراردادها
    field_lables = {field.name:field.verbose_name for field in Contract._meta.get_fields() if field.concrete}  # استخراج نام فیلدها
    
    
    query = request.GET.get('q','')
    contracts_table_1 = Contract.objects.all()
    if query: 
        contracts_table_1 = contracts_table_1.filter(full_name = query)
        contracts_table_1 = contracts_table_1[:4]

    # contracts_table_2 = Contract.objects.all()    
    selected_fields_1 = [ "full_name","national_id", "date_of_birth","contact_number",
                            "contract_type", "contract_number","bank_name_salary","IBAN_salary"]
    field_lables_selected_1 = {field.name:field.verbose_name for field in Contract._meta.get_fields() if field.name in selected_fields_1}



    return render(request, 'contracts/personel.html', {
                                                            'contracts_table_1': contracts_table_1,
                                                            'contracts_table_2': contracts_table_2,
                                                            'field_lables': field_lables,
                                                            'field_lables_selected_1':field_lables_selected_1,
                                                            'query': query})

def outstanding_view(request):
    return render(request, 'contracts/outstanding.html')

def nda_view(request):
    return render(request, 'contracts/nda.html')

def partnership_view(request):
    return render(request, 'contracts/partnership.html')

