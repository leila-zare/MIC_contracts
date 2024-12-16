from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import ContractForm
from django.contrib import messages
from .models import Contract
from django.db.models import Q
# from django.
from jalali_date import datetime2jalali, date2jalali
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


    # print("Contracts:", contracts)
    # print("Field lables:", field_lables)

    return render(request, 'contracts/contract_list.html', {
                                                            'contracts_table_1': contracts_table_1,
                                                            'contracts_table_2': contracts_table_2,
                                                            'field_lables': field_lables,
                                                            'field_lables_selected_1':field_lables_selected_1,
                                                            'query': query})
    # return render(request, "contracts/contract_list.html", {'contracts': contracts})

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

# def generate_pdf(request, contract_id):
#     contract = get_object_or_404(Contract, id = contract_id)
#     html_contract = render_to_string('contracts/pdf_tamplate.html',{'contract':contract})
#     pdf = HTML(string=html_contract).write_pdf()
#     response = HttpResponse(pdf,contract_type = 'application/pdf')
#     response['Contract_disposition'] = f"attachment;filename='contract_{contract_id}.pdf'"
#     return response
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import arabic_reshaper 
from bidi.algorithm import get_display
# # مرتب سازی راست چین
# def process_farsi_text(text):
#      reshaped_text = arabic_reshaper.reshape(text)
#      bidi_text = get_display(reshaped_text)
#      return bidi_text

# def generate_pdf(request, contract_id):

#     # دریافت اطلاعات قرارداد و کارمند از دیتابیس
#     contract = Contract.objects.get(id=contract_id)
#     # employee = contract.employee  # فرض: اطلاعات کارمند مرتبط با قرارداد است

#     # ایجاد پاسخ HTTP
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="contract-{contract_id}.pdf"'

    # # ایجاد PDF
    # p = canvas.Canvas(response, pagesize=A4)
    # width, height = A4  # عرض و ارتفاع صفحه
    # pdfmetrics.registerFont(TTFont('BNazanin', 'contracts/static/contracts/fonts/BNazanin.ttf'))
    # p.setFont("BNazanin", 12)
    # # نوشتن اطلاعات ثابت و پویا در PDF

    # عنوان قرارداد
    # p.drawCentredString(width / 2, height - 50, "قرارداد همکاری معین")
    # p.line(50, height - 60, width - 50, height - 60)

    # اطلاعات کارفرما و کارمند
    # p.drawRightString(300, height - 100, f"نام و نام خانوادگی: {contract.full_name}")
    # p.drawRightString(300, height - 120, f"کد ملی: {contract.national_id}")
    # p.drawRightString(300, height - 140, f"تاریخ تولد: {contract.date_of_birth}")
    # p.drawRightString(300, height - 160, f"محل سکونت: {contract.address }")

    # # اطلاعات قرارداد
    # p.drawString(300, height - 200, f"شماره قرارداد: {contract.contact_number}")
    # p.drawString(300, height - 220, f"تاریخ شروع: {contract.contract_start_date}")
    # p.drawString(300, height - 240, f"تاریخ پایان: {contract.contract_end_date}")
    # p.drawString(300, height - 260, f"مبلغ قرارداد: {contract.declared_salary} ریال")

    # متن اصلی قرارداد
    # contract_text = f"""
    # این قرارداد به شماره {contract.contact_number} فی‌مابین شرکت برهان رایان متین 
    # و آقا/خانم {contract.full_name} منعقد گردید. 
    # مدت این قرارداد از تاریخ {contract.contract_start_date} تا {contract.contract_end_date} می‌باشد.
    # مبلغ قرارداد برابر با {contract.declared_salary} ریال است.
    # """
    # contract_text = process_farsi_text(contract_text)

    
    # text_object = p.beginText(width - 200 ,height - 400)
    # # شروع از راست بالا
    # text_object.setFont("BNazanin", 10)
    # text_object.setTextOrigin(width - 200 ,height - 400)
    # # text_object.setTextAlign('')
    # for line in contract_text.split('\n'):
    #     text_object.textLine(line)
    # p.drawText(text_object)

    # # امضای کارفرما و کارمند
    # p.drawString(50, 100, "امضای کارفرما:")
    # p.drawString(300, 100, "امضای کارمند:")

    # # پایان
    # p.showPage()
    # p.save()

    # return response


from django.template.loader import render_to_string
from django.http import HttpResponse
from xhtml2pdf import pisa
def generate_pdf(request, contract_id):
    # دریافت اطلاعات قرارداد و کارمند
    contract = Contract.objects.get(id=contract_id)
    pdfmetrics.registerFont(TTFont('Vazir', 'contracts/static/contracts/fonts/BNazanin.ttf'))
    # رندر قالب HTML با داده‌ها
    html = render_to_string('contracts/generate_pdf.html', {'contract': contract})

    # تبدیل HTML به PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="contract-{contract_id}.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)

    # بررسی موفقیت‌آمیز بودن تولید PDF
    if pisa_status.err:
        return HttpResponse('خطا در تولید PDF', status=500)
    return response

def success_view(request):
    return render(request, 'contracts/sidebarlist.html')

     
















     

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


