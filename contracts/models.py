from django.db import models

# Create your models here.
    # class Meta:
    #     managed = False
    #     db_table = 'salary_contract'

# class SearchBox_personel(models.Model):
#     pass

class Contract(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    CONTRACT_TYPE_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Temporary', 'Temporary'),
        # Other contract types
    ]

    INSURANCE_TYPE_CHOICES = [
        ('Basic', 'Basic'),
        ('Comprehensive', 'Comprehensive'),
        # Other insurance types
    ]

    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contract_type = models.CharField(max_length=20, choices=CONTRACT_TYPE_CHOICES)
    contract_number = models.CharField(max_length=50, unique=True)
    fathers_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    national_id = models.CharField(max_length=10, unique=True)
    place_of_issue = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    address = models.TextField()
    position = models.CharField(max_length=100)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    housing_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    food_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    seniority_pay = models.DecimalField(max_digits=10, decimal_places=2)
    monthly = models.BooleanField(default=True)
    child_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    marriage_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    transportation_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    attraction_bonus = models.DecimalField(max_digits=10, decimal_places=2)
    management_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    hourly_wage = models.DecimalField(max_digits=10, decimal_places=2)
    hourly_wage_with_accord = models.DecimalField(max_digits=10, decimal_places=2)
    declared_salary = models.DecimalField(max_digits=10, decimal_places=2)
    insurance_type = models.CharField(max_length=20, choices=INSURANCE_TYPE_CHOICES)
    job_group = models.CharField(max_length=50)
    account_number = models.CharField(max_length=20)
    bank = models.CharField(max_length=50)

    def str(self):
        return f"Contract {self.contract_number} - {self.full_name}"