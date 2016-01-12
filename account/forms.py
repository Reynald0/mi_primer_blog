# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class RegisterUser(forms.Form):
    username = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(min_length=5,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    photo = forms.ImageField(required=False)

    def clean_username(self):
        #Comprueba que no exista un username igual en la base de datos
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('El nombre de usuario ya existe!')
        return username

    def clean_email(self):
        #Comprueba que no exista un email igual en la base de datos
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('El correo ya fue registrado!')
        return email

    def clean_password2(self):
        #Comprueba que password y password2 sean iguales
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2

class LogUser(forms.Form):
    username = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_user(self):
        #Comprueba que exista un username en la base de datos
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username):
            raise forms.ValidationError('El nombre de usuario no existe!')
        return username
