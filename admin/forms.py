from django import forms
from blog.models import Categories,Posts,ForbiddenWords,Tags
from django.contrib.auth.models import User
class CategoryForm(forms.ModelForm):
	class Meta:
		model=Categories
		fields=('category_name',)
class WordForm(forms.ModelForm):
	class Meta:
		model=ForbiddenWords
		fields=('word',)
class PostForm(forms.ModelForm):
	class Meta:
		model=Posts
		fields=('title','content','user','category','picture','tag',)
class TagForm(forms.ModelForm):
	class Meta:
		model=Tags
		fields=('tag_name',)
class UserForm (forms.ModelForm):
	class Meta:
		model=User
		fields=('first_name','last_name','username','email','password')