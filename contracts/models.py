

from django.db import models

class Contract(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="نام و نام خانوادگی")
    national_id = models.CharField(max_length=10, verbose_name="کد ملی")
    ID_number = models.CharField(max_length=10, verbose_name="شماره شناسنامه")
    date_of_birth = models.DateField(verbose_name="تاریخ تولد")
    place_of_issue = models.CharField(max_length=100, verbose_name="محل صدور")
    fathers_name = models.CharField(max_length=255, verbose_name="نام پدر")
    marital_status = models.CharField(max_length=20, choices=[
        ('single', 'مجرد'),
        ('married', 'متأهل'),
        ('divorced', 'طلاق گرفته'),
        ('widowed', 'بیوه')
    ], verbose_name="وضعیت تاهل")
    child_number = models.PositiveIntegerField(verbose_name="تعداد فرزند")
    contact_number = models.CharField(max_length=15, verbose_name="شماره تماس")
    military_status = models.CharField(max_length=20, choices=[
        ('exempt', 'معاف'),
        ('serving', 'در حال خدمت'),
        ('served', 'پایان خدمت')
    ], verbose_name="وضعیت نظام وظیفه")
    email = models.EmailField(verbose_name="آدرس ایمیل")
    reference = models.CharField(max_length=255, verbose_name="معرف")
    postal_code = models.CharField(max_length=10, verbose_name="کد پستی")
    address = models.TextField(verbose_name="آدرس")


    contract_type = models.CharField(max_length=100, choices=[
        ('Specific', 'معین'),
        ('Pseudo_specific', 'شبه معین '),
        ('Temporary', 'موقت')
    ], verbose_name="نوع قرارداد")
    contract_number = models.CharField(max_length=50, verbose_name="شماره قرارداد")
    contract_start_date = models.DateField(verbose_name="تاریخ شروع قرارداد")
    contract_end_date = models.DateField(verbose_name="تاریخ پایان قرارداد")
    job_group = models.CharField(max_length=100, verbose_name="گروه کاری")
    job_position = models.CharField(max_length=100, verbose_name="سمت شغلی")
    insurance_type = models.CharField(max_length=100, choices=[
        ('employer', 'کارفرما'),
        ('employee', 'کارمند'),
    ], verbose_name="نوع بیمه")
    declared_salary = models.CharField(max_length=100, choices=[
        ('Basic', 'پایه'),
        ('Real', 'واقعی'),
    ], verbose_name="حقوق ابرازی")
    base_salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="حقوق پایه")
    housing_allowance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="حق مسکن")
    food_allowance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="حق خوار و بار")
    seniority_pay = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="پایه سنوات")
    # monthly = models.BooleanField(default=True, verbose_name="ماهانه")
    child_allowance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="حق اولاد")
    marriage_allowance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="حق تاهل")
    transportation_allowance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ایاب و ذهاب")
    attraction_bonus = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="فوق العاده جذب")
    management_allowance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="حق مدیریت")
    hourly_wage = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="دستمزد ساعتی")
    hourly_wage_with_accord = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="دستمزد ساعتی با آکورد")
    insurance_number = models.CharField(max_length=10, verbose_name="شماره بیمه")
    
    bank_name_salary = models.CharField(max_length=100, verbose_name="نام بانک حقوق")
    account_number_salary = models.CharField(max_length=20, verbose_name="شماره حساب حقوق")
    IBAN_salary = models.CharField(max_length=34, verbose_name="شماره شبا حقوق")
    bank_name_petty_cash = models.CharField(max_length=100, verbose_name="نام بانک تنخواه")
    account_number_petty_cash = models.CharField(max_length=20, verbose_name="شماره حساب تنخواه")
    IBAN_petty_cash = models.CharField(max_length=34, verbose_name="شماره شبا تنخواه")
    
    def str(self):
        return self.full_name




# class Contract(models.Model):
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#     ]

#     CONTRACT_TYPE_CHOICES = [
#         ('Full-time', 'Full-time'),
#         ('Part-time', 'Part-time'),
#         ('Temporary', 'Temporary'),
#         # Other contract types
#     ]

#     INSURANCE_TYPE_CHOICES = [
#         ('Basic', 'Basic'),
#         ('Comprehensive', 'Comprehensive'),
#         # Other insurance types
#     ]

#     full_name = models.CharField(max_length=100)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     contract_type = models.CharField(max_length=20, choices=CONTRACT_TYPE_CHOICES)
#     contract_number = models.CharField(max_length=50, unique=True)
#     fathers_name = models.CharField(max_length=50)
#     date_of_birth = models.DateField()
#     national_id = models.CharField(max_length=10, unique=True)
#     place_of_issue = models.CharField(max_length=100)
#     contact_number = models.CharField(max_length=20)
#     address = models.TextField()
#     position = models.CharField(max_length=100)
#     contract_start_date = models.DateField()
#     contract_end_date = models.DateField()
#     base_salary = models.DecimalField(max_digits=10, decimal_places=2)
#     housing_allowance = models.DecimalField(max_digits=10, decimal_places=2)
#     food_allowance = models.DecimalField(max_digits=10, decimal_places=2)
#     seniority_pay = models.DecimalField(max_digits=10, decimal_places=2)
#     monthly = models.BooleanField(default=True)
#     child_allowance = models.DecimalField(max_digits=10, decimal_places=2)
#     marriage_allowance = models.DecimalField(max_digits=10, decimal_places=2)
#     transportation_allowance = models.DecimalField(max_digits=10, decimal_places=2)
#     attraction_bonus = models.DecimalField(max_digits=10, decimal_places=2)
#     management_allowance = models.DecimalField(max_digits=10, decimal_places=2)
#     hourly_wage = models.DecimalField(max_digits=10, decimal_places=2)
#     hourly_wage_with_accord = models.DecimalField(max_digits=10, decimal_places=2)
#     declared_salary = models.DecimalField(max_digits=10, decimal_places=2)
#     insurance_type = models.CharField(max_length=20, choices=INSURANCE_TYPE_CHOICES)
#     job_group = models.CharField(max_length=50)
#     account_number = models.CharField(max_length=20)
#     bank = models.CharField(max_length=50)

#     def str(self):
#         return f"Contract {self.contract_number} - {self.full_name}"