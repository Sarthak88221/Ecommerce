from django.contrib.auth import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class userform(UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            'type':'text',
            'id':'form3Example1cg',
            'class':'form-control form-control-lg' ,
        })
        self.fields['email'].widget.attrs.update({
            'type':'email',
            'id':'form3Example3cg',
            'class':'form-control form-control-lg' ,
            
        })
        self.fields['password1'].widget.attrs.update({
            'type':'password',
            'id':'form3Example4cdg',
            'class':'form-control form-control-lg' ,
        })
        self.fields['password2'].widget.attrs.update({
            'type':'password',
            'id':'form3Example4cdg',
            'class':'form-control form-control-lg' ,
        })
    class Meta:   
        model = User
        fields=['username','email','password1','password2']
