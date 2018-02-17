from django.shortcuts import render
from .models import Categories, Posts
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import RegUserForm
from django.contrib.auth import authenticate , login , logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.models import User
from .models import Likes
from django.http import JsonResponse



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
    usr_form=RegUserForm()

    if request.method=="POST":
        users = User.objects.all().filter(email=request.POST['email'])
        if users.exists():
            return render(request, "login&&register/registeration.html", {"form": usr_form, "dublemail": 1})
        usr_form = RegUserForm(request.POST)
        if usr_form.is_valid():
            usr_form.save()
            return HttpResponseRedirect("/blog/homepage")
    return render(request, "login&&register/registeration.html",{"form":usr_form})


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


def getProduct(request,post_id):
    pst=Posts.objects.filter(id=post_id)
    countlikes = Likes.objects.all().filter(state=1, post=pst).count()
    countdislike = Likes.objects.all().filter(state=0, post=pst).count()
    context={"post":pst[0] , "plikes":countlikes ,"pdislike":countdislike}
    return render(request,"postdetails/get_post.html",context)


def makelike(request,post_id):
    if request.user.is_authenticated():
            post = Posts.objects.filter(id=post_id)

            record=Likes.objects.all().filter(state=1, user=request.user, post=post[0])
            if record.exists():
                deletelike=Likes.objects.get(state=1, user=request.user, post=post[0])
                deletelike.delete()
            else:
                Likes.objects.create(state=1, user=request.user, post=post[0])



    return HttpResponse("data")


def makedislike(request,post_id):
    if request.user.is_authenticated():
            post = Posts.objects.filter(id=post_id)
            record=Likes.objects.all().filter(state=0, user=request.user, post=post[0])
            if record.exists():
                deletelike=Likes.objects.get(state=0, user=request.user, post=post[0])
                deletelike.delete()
            else:
                Likes.objects.create(state=0, user=request.user, post=post[0])



    return JsonResponse({'foo': 'bar'})








