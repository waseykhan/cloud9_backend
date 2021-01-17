import django import forms

class FormName(forms.Form):
    FirstName = forms.CharField(max_length=30, required=True)
    LastName = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=60, required=True)
    pas = forms.CharField(widget=PasswordInput(), required=False)
    confPas = forms.CharField(widget=PasswordInput(), required=False)