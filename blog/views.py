from django.shortcuts import render
from .models import Categories, Posts
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UserForm
from django.contrib.auth import authenticate , login , logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import  login_required

def homepage(request):
    context = {'homepage': Categories.objects.all(), 'allCategories':Categories.objects.all(), 'allPosts':Posts.objects.all()[:5]}
    return render(request, 'homepage/homepage.html', context)

def search(request):

    found_entries = Posts.objects.filter(title__icontains=request.POST['term']).order_by('created_at')
    context = {"found": found_entries}
    return render(request, "search.html", context)



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse("you are loggin")



def register(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
            return HttpResponseRedirect('/blog/home')

        else:
            #print(user_form.errors)
            pass

    else:
        user_form = UserForm()
        return render(request,"registeration.html",{"user_form":user_form , "registered":registered})




def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Acount Not Active Please Contact With Admin")
        else:
            return HttpResponse("invalid user name and password")

    else:
        return render(request,'login.html',{})


