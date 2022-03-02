from django import forms

class student_form(forms.Form):
    sid=forms.IntegerField(label="enter student id:")
    sname=forms.CharField(label="enter student name:",max_length=30)
    
