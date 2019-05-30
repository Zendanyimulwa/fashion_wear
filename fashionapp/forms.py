from django import forms
from . models import Clothe,User


class ClotheForm(forms.ModelForm):
    class Meta:
        model = Clothe
        fields = ('material','type','cover',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email','password')


