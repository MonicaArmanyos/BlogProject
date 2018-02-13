from datetime import datetime
from django.db import models


class User(models.Model):
	user_name = models.CharField(max_length = 50)
	email=models.EmailField(max_length = 60)
	password=models.CharField(max_length = 10)
	created_at=models.DateField(default=datetime.now, blank=True)
	is_admin=models.BooleanField()
	is_blocked=models.BooleanField()
	def __str__(self):
		return self.user_name
	def __str__(self):
		return self.email
	def __str__(self):
		return self.created_at
	def __str__(self):
		return self.is_admin
	def __str__(self):
		return self.is_blocked




class Category(models.Model):
	cat_name=models.CharField(max_length = 50)
	user = models.ManyToManyField(User)
	def __str__(self):
		return self.cat_name

class Posts(models.Model):
	title=models.CharField(max_length = 50)
	created_at = models.DateField(default=datetime.now, blank=True)
	picture=models.ImageField()
	content=models.CharField(max_length = 200)
	user = models.ForeignKey(User)
	cat=models.ForeignKey(Category)
	def __str__(self):
		return self.title
	def __str__(self):
		return self.content
	def __str__(self):
		return self.picture
	def __str__(self):
		return self.cat
	def __str__(self):
		return self.user
	def __str__(self):
		return self.created_at

class Comments(models.Model):
	content=models.CharField(max_length = 200)
	user = models.ForeignKey(User)
	post=models.ForeignKey(Posts)
	def __str__(self):
		return self.content
	def __str__(self):
		return self.user
	def __str__(self):
		return self.post

class Replay(models.Model):
	content = models.CharField(max_length=200)
	user = models.ForeignKey(User)
	#post = models.ForeignKey(Posts)
	comment=models.ForeignKey(Comments)
	def __str__(self):
		return self.content
	def __str__(self):
		return self.user
	def __str__(self):
		return self.comment

class Likes(models.Model):
	type=models.IntegerField()
	post = models.ForeignKey(Posts)
	def is_like(self):
		countlike=0
		countdislike=0
		if (self.type == 1):
			countlike+=1
		elif(self.type == 0):
			countdislike += 1
	def __str__(self):
		return self.type
	def __str__(self):
		return self.post

class Tags(models.Model):
	tag_name=models.CharField(max_length = 15)
	post = models.ForeignKey(Posts)
	def __str__(self):
		return self.tag_name
	def __str__(self):
		return self.post

class ForbiddenWords(models.Model):
	word=models.CharField(max_length = 15)
	def __str__(self):
		return self.word

