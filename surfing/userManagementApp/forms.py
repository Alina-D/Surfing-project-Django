from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=48, required=True, \
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Логин'}))
    email = forms.EmailField(label='Е-маил', required=True,
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'E-mail'}))
    password1 = forms.CharField(label='Пароль', max_length=36, \
        help_text='Пароль должен отличаться от логина.',\
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Пароль'}))
    password2 = forms.CharField(label='Пароль', max_length=36, help_text='Повторите пароль', \
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Пароль'}))
    first_name = forms.CharField(label='Имя', max_length=36, \
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Имя'}))
    last_name = forms.CharField(label='Фамилия', max_length=48, \
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Фамилия'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')


class UserChangeForm(forms.ModelForm):
    username = forms.CharField(label='Логин', max_length=48, required=True, \
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Логин'}))
    email = forms.EmailField(label='Е-маил', required=True,
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'E-mail'}))
    first_name = forms.CharField(label='Имя', max_length=36, \
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Имя'}))
    last_name = forms.CharField(label='Фамилия', max_length=48, \
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Фамилия'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
#       fields = ('__all__')       