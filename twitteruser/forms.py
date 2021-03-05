from django import forms


# Signup form
class SignupForm(forms.Form):
    username = forms.CharField(max_length=120)
    email = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)
