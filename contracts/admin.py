from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Contract)
# @admin.register(models.Contract)
# class ContractAdmin(admin.ModelAdmin):
#     list_display = (
#         "full_name",
#         "marital_status",
#         "child_number",
#         "hourly_wage",
#     )
    