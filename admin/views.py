from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Categories,Posts,ForbiddenWords
from django.contrib.auth.models import User
from .forms import PostForm,CategoryForm,WordForm
from django.http import HttpResponseRedirect

# Create your views here.

def dashBoard(request):
	return render(request,"admin.html")
def allPosts(request):
	context={"allPosts":Posts.objects.all()}
	return render(request,"posts.html",context)
def addPost(request):
	form=PostForm()
	if request.method=="POST":
		form=PostForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
	                return HttpResponseRedirect('/admin/allPosts')
	return render(request,"newPost.html",{'form':form})
	
	
def editPost(request,post_id):
	form=PostForm()
	post=Posts.objects.get(id=post_id)
	if request.method=="POST":
		form=PostForm(request.POST,request.FILES,instance=post)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/admin/allPosts')
	else:
		form=PostForm(instance=post)
	return render(request,"editPost.html",{'form':form})	
	
def deletePost(request,post_id):
	post=Posts.objects.get(id=post_id)
	post.delete()
	return HttpResponseRedirect('/admin/allPosts') 
	
def allCategories(request):
	context={"allCategories":Categories.objects.all()}
	return render(request,"categories.html",context)
def addCategory(request):
	form=CategoryForm()
	if request.method=="POST":
		form=CategoryForm(request.POST)
		if form.is_valid():
			form.save()
	                return HttpResponseRedirect('/admin/allCategories')
	return render(request,"newCategory.html",{'form':form})
	
	
def editCategory(request,category_id):
	form=CategoryForm()
	category=Categories.objects.get(id=category_id)
	if request.method=="POST":
		form=CategoryForm(request.POST,instance=category)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/admin/allCategories')
	else:
		form=CategoryForm(instance=category)
	return render(request,"editCategory.html",{'form':form})	
	
def deleteCategory(request,category_id):
	category=Categories.objects.get(id=category_id)
	category.delete()
	return HttpResponseRedirect('/admin/allCategories')     	

def allWords(request):
	context={"allWords":ForbiddenWords.objects.all()}
	return render(request,"words.html",context)
def addWord(request):
	form=WordForm()
	if request.method=="POST":
		form=WordForm(request.POST)
		if form.is_valid():
			form.save()
	                return HttpResponseRedirect('/admin/allWords')
	return render(request,"newWord.html",{'form':form})
	


def editWord(request,word_id):
	form=WordForm()
	word=ForbiddenWords.objects.get(id=word_id)
	if request.method=="POST":
		form=WordForm(request.POST,instance=word)
		if form.is_valid():
			form.save()
	        return HttpResponseRedirect('/admin/allWords')
	else:
		form=WordForm(instance=word)
	return render(request,"editWord.html",{'form':form})	
	

def deleteWord(request,word_id):
    word=Words.objects.get(id=word_id)
    word.delete()
    return HttpResponseRedirect('/admin/allWords')
