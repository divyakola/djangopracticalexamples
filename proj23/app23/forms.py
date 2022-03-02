from django import forms
from .models import EmployeModel

class EmployeForm(forms.ModelForm):
    class Meta:
        model=EmployeModel
        fields="__all__"
