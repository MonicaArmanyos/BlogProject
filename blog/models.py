from datetime import datetime
from django.db import models
from django.contrib.auth.models import User



class Categories(models.Model):
	category_name=models.CharField(max_length = 50)
	user = models.ManyToManyField(User)
	def __str__(self):
		return self.category_name

class Posts(models.Model):
	title=models.CharField(max_length = 50)
	created_at = models.DateField(default=datetime.now, blank=True)
	picture=models.ImageField()
	content=models.CharField(max_length = 200)
	user = models.ForeignKey(User)
	category=models.ForeignKey(Categories)
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
	type=models.IntegerField()
	post = models.ForeignKey(Posts)
	def __str__(self):
		return self.type


class Tags(models.Model):
	tag_name=models.CharField(max_length = 15)
	post = models.ManyToManyField(Posts,related_name='post_tags')
	#related_name is the name you use when accessing the model from the related one(Posts model)
	def __str__(self):
		return self.tag_name


class ForbiddenWords(models.Model):
	word=models.CharField(max_length = 15)
	def __str__(self):
		return self.word
