from django import forms
from .models import Employee, Company


class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class UpdateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
