from django import forms
from blog.models import Categories,Posts,ForbiddenWords
from django.contrib.auth.models import User
class CategoryForm(forms.ModelForm):
	class Meta:
		model=Categories
		fields=('category_name','user',)
class WordForm(forms.ModelForm):
	class Meta:
		model=ForbiddenWords
		fields=('word',)
class PostForm(forms.ModelForm):
	class Meta:
		model=Posts
		fields=('title','content','user','category','picture',)
