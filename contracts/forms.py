from django import forms
from . import models

class ContractForm(forms.ModelForm):
    class Meta:
        model = models.Contract
        fields = '__all__' 
