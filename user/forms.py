from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

class LoginForm(forms.Form):
    username = forms.CharField(label='Kullanici Adi')
    password = forms.CharField(label='Parola',widget=forms.PasswordInput)
    
class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField(required=True, label="E-posta Adresi")

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        # user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})