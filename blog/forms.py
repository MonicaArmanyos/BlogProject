from django import forms
from django.contrib.auth.models import User
from .models import Comments , Replies

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('first_name','last_name','username','email','password')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=('text',)

class ReplyForm(forms.ModelForm):
    class Meta:
        model=Replies
        fields=('text',)
