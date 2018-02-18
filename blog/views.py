from django.shortcuts import render
from .models import Categories, Posts, Tags , Comments , Replies , ForbiddenWords
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
    return  render(request,"index.html")

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


def post(request,post_id):
    pst=Posts.objects.get(id=post_id)
    ctg=Categories.objects.get(id=pst.category_id)
    Alltags=pst.post_tags.filter(post=post_id)
    #or Alltags=pst.post_tags.all() would also give all the tags of the post
    forbiddenWords=[]
    Rej_words=ForbiddenWords.objects.all()
    for word in Rej_words:
        forbiddenWords.append(word.word)
    comments=Comments.objects.filter(post_id=post_id)
    for comment in comments:
        words=comment.text.split()
        comment.text=""
        for comm_word in words:
            if comm_word in forbiddenWords:
                comm_word='*'*len(comm_word)
            comment.text+=" "+comm_word
    replies=Replies.objects.filter(comment_id__in=comments)
    context={'post':pst,'category':ctg.category_name,'tags':Alltags,'comments':comments,'replies':replies}
    return render(request, 'post.html',context)

def comment(request):
    pass

def reply(requst):
    pass