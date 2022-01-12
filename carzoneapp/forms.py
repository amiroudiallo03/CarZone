from django import forms


class SignupForm(forms.Form):
    firstname = forms.CharField(max_length=255, required=False)
    lastname = forms.CharField(max_length=255, required=False)
    username = forms.CharField(min_length=4, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=4, widget=forms.PasswordInput())

    