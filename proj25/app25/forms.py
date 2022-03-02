from django import forms
from .models import emp
#create your forms here
class empForm(forms.ModelForm):
    class Meta:
        model=emp
        fields="__all__"
