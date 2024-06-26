from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'form-control'}) )

    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password1','password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

             
        

class LoginForm(forms.Form):
        username = forms.CharField(max_length=150,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=150, required=True)
        
