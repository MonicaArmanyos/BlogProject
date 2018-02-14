from django.shortcuts import render
from .models import Categories, Posts
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UserForm
from django.contrib.auth import authenticate , login , logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import  login_required

def homepage(request):
    context = {'homepage': Categories.objects.all(), 'allCategories':Categories.objects.all(), 'allPosts':Posts.objects.all()}
    return render(request, 'homepage/homepage.html', context)


def index(request):
    return  render(request,"homepage.html")

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
            return HttpResponseRedirect('/blog/homepage')

        else:
            #print(user_form.errors)
            pass

    else:
        user_form = UserForm()
        return render(request, "login&&register/registeration.html", {"user_form":user_form , "registered":registered})




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
                return render(request, 'login&&register/login.html', {'info': 0}) #user Not Active
        else:
            return render(request, 'login&&register/login.html', {'info':1}) #error in username or password

    else:
        return render(request, 'login&&register/login.html', {})


