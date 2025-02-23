from django import forms
from contracts.models import Contract
from django_jalali.forms import jDateField as jalaliDateField
from django_jalali.admin.widgets import AdminjDateWidget
# from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
# from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

class ContractForm(forms.ModelForm):
    date_of_birth = jalaliDateField(widget = AdminjDateWidget)
    contract_start_date = jalaliDateField(widget = AdminjDateWidget)
    contract_end_date = jalaliDateField(widget = AdminjDateWidget)
    class Meta:
        model = Contract
        fields = '__all__'
        # fields = [
        #         "full_name",
        #         "contract_type",
        #         "contract_number",
        #         "fathers_name",
        #         "date_of_birth",
        #         "national_id",
        #         "ID_number",
        #         "place_of_issue",
        #         "marital_status",
        #         "child_number",
        #         "military_status",
        #         "contact_number",
        #         "email",
        #         "reference",
        #         "postal_code",
        #         "address",
        #         "job_position",
        #         "contract_start_date",
        #         "contract_end_date",
        #         "base_salary",
        #         "housing_allowance",
        #         "food_allowance",
        #         "seniority_pay",
        #         "child_allowance",
        #         "marriage_allowance",
        #         "transportation_allowance",
        #         "attraction_bonus",
        #         "management_allowance",
        #         "hourly_wage",
        #         "hourly_wage_with_accord",
        #         "declared_salary",
        #         "insurance_type",
        #         "job_group",
        #         "account_number_salary",
        #         "IBAN_salary",
        #         "bank_name_salary",
        #         "account_number_petty_cash",
        #         "IBAN_petty_cash",
        #         "bank_name_petty_cash",
        # ]
        # widgets = {
        #         "full_name":"نام و نام خانوادگی",
        #         "contract_type":"نوع قرارداد",
        #         "contract_number":"شماره قرارداد",
        #         "fathers_name":"نام پدر",
        #         "date_of_birth":"تاریخ تولد",
        #         "national_id":"کد ملی",
        #         "ID_number":"شماره شناسنامه",
        #         "place_of_issue":"محل صدور",
        #         "matiral_status":"وضعیت تاهل",
        #         "child_number":"تعداد فرزند",
        #         "military_status":"وضعیت نظام وظیفه",
        #         "contact_number":"شماره تماس",
        #         "Imail":"آدرس ایمیل",
        #         "refrence": "معرف",
        #         "postal_code":"تعداد فرزند",
        #         "address":"آدرس",
        #         "position":" سمت شغلی",
        #         "contract_start_date":"تاریخ شروع قرارداد",
        #         "contract_end_date":"تاریخ پایان قرارداد",
        #         "base_salary":"حقوق پایه",
        #         "housing_allowance":"حق مسکن",
        #         "food_allowance":"حق خوار و بار",
        #         "seniority_pay":"پایه سنوات",
        #         "monthly":"ماهانه",
        #         "child_allowance":"حق اولاد",
        #         "marriage_allowance":"حق تاهل",
        #         "transportation_allowance":"ایاب و ذهاب",
        #         "attraction_bonus":"فوق العاده جذب",
        #         "management_allowance":"حق مدیریت",
        #         "hourly_wage":"دستمزد ساعتی",
        #         "hourly_wage_with_accord":"دستمزد ساعتی با آکورد",
        #         "declared_salary":"حقوق ابرازی",
        #         "insurance_type":"نوع بیمه",
        #         "job_group":"گروه کاری",
        #         "account_number_salary":"شماره حساب حقوق",
        #         "IBAN_salary":"شماره شبا حقوق",
        #         "bank_name_salary":"نام بانک حقوق",
        #         "account_number_petty_cash":"شماره حساب تنخواه",
        #         "IBAN_petty_cash":"شماره شبا تنخواه",
        #         "bank_name_petty_cash":"نام بانک تنخواه",
        #     }

        labels = {
                "full_name":"نام و نام خانوادگی",
                "contract_type":"نوع قرارداد",
                "contract_number":"شماره قرارداد",
                "fathers_name":"نام پدر",
                "date_of_birth":"تاریخ تولد",
                "national_id":"کد ملی",
                "ID_number":"شماره شناسنامه",
                "place_of_issue":"محل صدور",
                "marital_status":"وضعیت تاهل",
                "child_number":"تعداد فرزند",
                "military_status":"وضعیت نظام وظیفه",
                "contact_number":"شماره تماس",
                "email":"آدرس ایمیل",
                "reference": "معرف",
                "postal_code":"تعداد فرزند",
                "address":"آدرس",
                "job_position":" سمت شغلی",
                "contract_start_date":"تاریخ شروع قرارداد",
                "contract_end_date":"تاریخ پایان قرارداد",
                "base_salary":"حقوق پایه",
                "housing_allowance":"حق مسکن",
                "food_allowance":"حق خوار و بار",
                "seniority_pay":"پایه سنوات",
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
        error_messages = {
                "full_name":{'required': ' فیلد زیر را حتما وارد کنید', 'invalid':'مقدار وارد شده معتبر نیست'},
                "contract_type":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "contract_number":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "fathers_name":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "date_of_birth":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "national_id":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "ID_number":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "place_of_issue":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "marital_status":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "child_number":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "military_status":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "contact_number":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "email":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "reference": {'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "postal_code":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "address":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "job_position":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "contract_start_date":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "contract_end_date":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "base_salary":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "housing_allowance":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "food_allowance":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "seniority_pay":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "child_allowance":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "marriage_allowance":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "transportation_allowance":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "attraction_bonus":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "management_allowance":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "hourly_wage":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "hourly_wage_with_accord":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "declared_salary":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "insurance_type":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "job_group":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "account_number_salary":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "IBAN_salary":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "bank_name_salary":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "account_number_petty_cash":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "IBAN_petty_cash":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
                "bank_name_petty_cash":{'required': 'وارد کردن این فیلد اجباری است', 'invalid':'مقدار وارد شده معتبر نیست'},
            }
        
        # def __init__(self, *args, **kwargs):
        #     super(ContractForm, self).__init__(*args, **kwargs)
        #     self.fields['date'] = JalaliDateField(label=('date'), # date format is  "yyyy-mm-dd"
        #     widget=AdminJalaliDateWidget # optional, to use default datepicker
        #     )

        #     # you can added a "class" to this field for use your datepicker!
        #     # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

        #     self.fields['date_time'] = SplitJalaliDateTimeField(label=('date time'), 
        #     widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        #     )
        def clean(self):
            cleaned_data = super().clean()
            marital_status = cleaned_data.get(marital_status)
            child_number = cleaned_data.get(child_number)

            if marital_status != "متأهل" and child_number > 0:
                forms.ValidationError('افراد مجرد نمی توانند تعداد فرزند داشته باشند.')
                return cleaned_data