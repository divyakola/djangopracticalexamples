from django import forms

class customer(forms.Form):
    cid=forms.IntegerField(label="Enter Customer Id:")
    cname=forms.CharField(label="Enter Customer Name:",max_length=30)
    cemail=forms.EmailField(label="Enter Customer Email:",
                            widget=forms.EmailInput())
    cpwd=forms.CharField(label="Enter Customer Password:",
                         widget=forms.PasswordInput(),
                         help_text="password contains atleats 8 charecters")
