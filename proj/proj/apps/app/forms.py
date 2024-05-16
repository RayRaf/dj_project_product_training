from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Product, Project


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Твое имя, сынку'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Секретный паоль'}))


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'projects': forms.CheckboxSelectMultiple,
        }