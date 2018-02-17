from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
	category_name=models.CharField(max_length = 50)
	user = models.ManyToManyField(User, through="CategoryUser")
	def __str__(self):
		return self.category_name

class CategoryUser (models.Model):
	category= models.ForeignKey(Categories)
	user= models.ForeignKey(User)

class Tags(models.Model):
	tag_name=models.CharField(max_length = 15)
	def __str__(self):
		return self.tag_name

class Posts(models.Model):
	title=models.CharField(max_length = 50)
	created_at = models.DateField(default=datetime.now, blank=True)
	picture=models.ImageField(upload_to='media',blank=True)
	content=models.CharField(max_length = 200)
	category=models.ForeignKey(Categories)
	tag = models.ManyToManyField(Tags)
	user = models.ForeignKey(User,related_name='author')
	def __str__(self):
		return self.title


class Comments(models.Model):
	text=models.CharField(max_length = 200)
	user = models.ForeignKey(User)
	post=models.ForeignKey(Posts)
	def __str__(self):
		return self.content


class Replies(models.Model):
	text = models.CharField(max_length=200)
	user = models.ForeignKey(User)
	comment=models.ForeignKey(Comments)
	def __str__(self):
		return self.text


class Likes(models.Model):
	state=models.IntegerField()
	user = models.ForeignKey(User)
	post = models.ForeignKey(Posts)
	def __str__(self):
		return self.state


class ForbiddenWords(models.Model):
	word=models.CharField(max_length = 15)
	def __str__(self):
		return self.word