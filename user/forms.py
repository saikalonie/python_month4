from django import forms

class  RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if (password and password_confirm) and (password != password_confirm):
            raise forms.ValidationError("Passwords do not match")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)




