
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import ContractForm
from django.contrib import messages
from .models import Contract
from django.db.models import Q
# from django.
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.forms.models import model_to_dict


# Create your views here.
# class ContractView(View)

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
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()  # ذخیره تغییرات در دیتابیس
            return redirect('contracts:contractlist')  # بازگشت به صفحه لیست قراردادها
    else:
        # اگر درخواست GET بود، فرم را با داده‌های رکورد پر کن
        form = ContractForm(instance=contract)

    return render(request, 'contracts/edit_contract.html', {'form': form}) 



# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.pdfbase import pdfmetrics
# from django.template.loader import render_to_string
# from django.http import HttpResponse
# from xhtml2pdf import pisa
# def generate_pdf(request, contract_id):
#     # دریافت اطلاعات قرارداد و کارمند
#     contract = Contract.objects.get(id=contract_id)
#     pdfmetrics.registerFont(TTFont('Vazir', 'contracts/static/contracts/fonts/BNazanin.ttf'))
#     # رندر قالب HTML با داده‌ها
#     html = render_to_string('contracts/generate_pdf.html', {'contract': contract})

#     # تبدیل HTML به PDF
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="contract-{contract_id}.pdf"'
#     pisa_status = pisa.CreatePDF(html, dest=response)

#     # بررسی موفقیت‌آمیز بودن تولید PDF
#     if pisa_status.err:
#         return HttpResponse('خطا در تولید PDF', status=500)
#     return response


from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def generate_pdf(request, contract_id):
    # دریافت اطلاعات قرارداد و کارمند
    contract = Contract.objects.get(id=contract_id)
    # ثبت فونت فارسی
    pdfmetrics.registerFont(TTFont('Vazir', 'contracts/static/contracts/fonts/Vazir-FD.ttf'))
    # رندر قالب HTML با داده‌ها
    # html = render_to_string('contracts/generate_pdf.html', {'contract': contract})

    # تبدیل HTML به PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="contract-{contract_id}.pdf"'
    # pisa_status = pisa.CreatePDF(html, dest=response)
    c = canvas.Canvas(response,pagesize=A4)
    c.setFont('Vazir', 12)
    c.drawString(100, 750, f'نام و نام خانوادگی: {contract.full_name}')
    c.drawString(100, 730, f'کد ملی : {contract.national_id}')
    c.drawString(100, 710, f'تاریخ شروع قرارداد: {contract.contract_start_date}')
    # بررسی موفقیت‌آمیز بودن تولید PDF
    # if pisa_status.err:
    #     return HttpResponse('خطا در تولید PDF', status=500)
    c.showPage()
    c.save()

    return response

    import WeasyPrint




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














     

# labels = {
#     "full_name":"نام و نام خانوادگی",
#     "contract_type":"نوع قرارداد",
#     "contract_number":"شماره قرارداد",
#     "fathers_name":"نام پدر",
#     "date_of_birth":"تاریخ تولد",
#     "national_id":"کد ملی",
#     "ID_number":"شماره شناسنامه",
#     "place_of_issue":"محل صدور",
#     "matiral_status":"وضعیت تاهل",
#     "child_number":"تعداد فرزند",
#     "military_status":"وضعیت نظام وظیفه",
#     "contact_number":"شماره تماس",
#     "Imail":"آدرس ایمیل",
#     "refrence": "معرف",
#     "postal_code":"تعداد فرزند",
#     "address":"آدرس",
#     "position":" سمت شغلی",
#     "contract_start_date":"تاریخ شروع قرارداد",
#     "contract_end_date":"تاریخ پایان قرارداد",
#     "base_salary":"حقوق پایه",
#     "housing_allowance":"حق مسکن",
#     "food_allowance":"حق خوار و بار",
#     "seniority_pay":"پایه سنوات",
#     "monthly":"ماهانه",
#     "child_allowance":"حق اولاد",
#     "marriage_allowance":"حق تاهل",
#     "transportation_allowance":"ایاب و ذهاب",
#     "attraction_bonus":"فوق العاده جذب",
#     "management_allowance":"حق مدیریت",
#     "hourly_wage":"دستمزد ساعتی",
#     "hourly_wage_with_accord":"دستمزد ساعتی با آکورد",
#     "declared_salary":"حقوق ابرازی",
#     "insurance_type":"نوع بیمه",
#     "job_group":"گروه کاری",
#     "account_number_salary":"شماره حساب حقوق",
#     "IBAN_salary":"شماره شبا حقوق",
#     "bank_name_salary":"نام بانک حقوق",
#     "account_number_petty_cash":"شماره حساب تنخواه",
#     "IBAN_petty_cash":"شماره شبا تنخواه",
#     "bank_name_petty_cash":"نام بانک تنخواه",
# }


