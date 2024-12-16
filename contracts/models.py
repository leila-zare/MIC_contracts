from django.db import models
from django_jalali.db import models as jmodels
from django.core.validators import MinValueValidator, MaxValueValidator

class Contract(models.Model):
    full_name = models.CharField(max_length=255,default='SOME STRING', verbose_name="نام و نام خانوادگی")
    national_id = models.CharField(max_length=10, default='SOME STRING',verbose_name="کد ملی")
    ID_number = models.CharField(max_length=100,default='SOME STRING', verbose_name="شماره شناسنامه")
    date_of_birth = jmodels.jDateField(verbose_name="تاریخ تولد")
    place_of_issue = models.CharField(max_length=100,default='SOME STRING', verbose_name="محل صدور")
    fathers_name = models.CharField(max_length=255, default='SOME STRING', verbose_name="نام پدر")
    marital_status = models.CharField(max_length=20,default='SOME STRING', choices=[
        ('متأهل', 'متأهل'),
        ('مجرد', 'مجرد'),
        # ('married', 'متأهل'),
        # ('single', 'مجرد'),
        # ('divorced', 'طلاق گرفته'),
        # ('widowed', 'بیوه')
    ], verbose_name="وضعیت تاهل")
    child_number = models.DecimalField(default=0, max_digits=10, decimal_places= 0,verbose_name="تعداد فرزند")
    contact_number = models.CharField(max_length=15, default='SOME STRING',verbose_name="شماره تماس")
    military_status = models.CharField(max_length=20, default='SOME STRING',choices=[
        ('معاف شده', 'معاف شده'),
        ('در حال خدمت', 'در حال خدمت'),
        ('پایان خدمت', 'پایان خدمت'),
        ('نیاز به خدمت ندارد', 'نیاز به خدمت ندارد'),
        ('معافیت تحصیلی', 'معافیت تحصیلی'),
        # ('exempt', 'معاف'),
        # ('serving', 'در حال خدمت'),
        # ('served', 'پایان خدمت'),
        # ('nothing', 'نیاز به خدمت ندارد'),
    ], verbose_name="وضعیت نظام وظیفه")
    email = models.EmailField(default='SOME STRING',verbose_name="آدرس ایمیل")
    reference = models.CharField(max_length=255,default='SOME STRING', verbose_name="معرف")
    postal_code = models.CharField(max_length=10, default='SOME STRING',verbose_name="کد پستی")
    address = models.TextField(default='SOME STRING', verbose_name="آدرس")
    degree_of_study = models.CharField(max_length=20, default='SOME STRING',choices=[
        ('سیکل', 'سیکل'),
        ('دیپلم', 'دیپلم'),
        ('فوق دیپلم', 'فوق دیپلم'),
        ('کارشناسی', 'کارشناسی'),
        ('کارشناسی ارشد', 'کارشناسی ارشد'),
        ('دکتری', 'دکتری'),
        ('فوق دکتری', 'فوق دکتری'),
        ('حوزوی', 'حوزوی'),
    ], verbose_name="مدرک تحصیلی")
    field_of_study = models.CharField(max_length=255,default='SOME STRING', verbose_name="رشته تحصیلی")
    contract_type = models.CharField(max_length=100, default='SOME STRING',choices=[
        ('معین', 'معین'),
        ('شبه معین', 'شبه معین'),
        ('ساعتی', 'ساعتی'),
        # ('Specific', 'معین'),
        # ('Pseudo_specific', 'شبه معین'),
        # ('Temporary', 'موقت'),
    ], verbose_name="نوع قرارداد")
    contract_number = models.CharField(max_length=50, default='SOME STRING',verbose_name="شماره قرارداد")
    contract_start_date = jmodels.jDateField(verbose_name="تاریخ شروع قرارداد")
    contract_end_date = jmodels.jDateField(verbose_name="تاریخ پایان قرارداد")
    job_group = models.CharField(max_length=100,default='SOME STRING', choices=[
        ('ستاد', 'ستاد'),
        ('مدیریت', 'مدیریت'),
        ('فنی', 'فنی'),
        ('بازرگانی', 'بازرگانی'),
        ('دفتر قم', 'دفتر قم'),
        # ('headquarters', 'ستاد'),
        # ('management', 'مدیریت'),
        # ('technical', 'فنی'),
    ],  verbose_name="گروه کاری")
    job_position = models.CharField(max_length=100,default='SOME STRING', verbose_name="سمت شغلی")
    insurance_type = models.CharField(max_length=100,default='SOME STRING', choices=[
        # ('employer', 'کارفرما'),
        # ('employee', 'کارمند'),
         ('کارفرما', 'کارفرما'),
        ('کارمند', 'کارمند'),
    ], verbose_name="نوع بیمه")
    declared_salary = models.CharField(max_length=100,default='SOME STRING', choices=[
        ('پایه', 'پایه'),
        ('واقعی', 'واقعی'),
        # ('Basic', 'پایه'),
        # ('Real', 'واقعی'),
    ], verbose_name="حقوق ابرازی")
    base_salary = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="حقوق پایه")
    housing_allowance = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="حق مسکن")
    food_allowance = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="حق خوار و بار")
    seniority_pay = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="پایه سنوات")
    # monthly = models.BooleanField(default=True, verbose_name="ماهانه")
    child_allowance = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="حق اولاد")
    marriage_allowance = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="حق تاهل")
    transportation_allowance = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="ایاب و ذهاب")
    attraction_bonus = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="فوق العاده جذب")
    management_allowance = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="حق مدیریت")
    hourly_wage = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="دستمزد ساعتی")
    hourly_wage_with_accord = models.IntegerField(verbose_name="درصد آکورد") 
    insurance_number = models.CharField(max_length=10, default='SOME STRING',verbose_name="شماره بیمه")
    
    bank_name_salary = models.CharField(max_length=100, default='SOME STRING', verbose_name="نام بانک حقوق")
    account_number_salary = models.CharField(max_length=100,default='SOME STRING',  verbose_name="شماره حساب حقوق")
    IBAN_salary = models.CharField(max_length=100, default='SOME STRING',  verbose_name="شماره شبا حقوق")
    # bank_name_petty_cash = models.CharField(max_length=100,default='SOME STRING',  verbose_name="نام بانک تنخواه")
    # account_number_petty_cash = models.CharField(max_length=100,default='SOME STRING', verbose_name="شماره حساب تنخواه")
    # IBAN_petty_cash = models.CharField(max_length=100, default='SOME STRING', verbose_name="شماره شبا تنخواه")
    
    def __str__(self):
        return self.full_name

