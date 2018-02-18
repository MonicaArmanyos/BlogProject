from django.shortcuts import render
from .models import Categories, Posts, Tags , Comments , Replies , ForbiddenWords
from django.http import HttpResponse , JsonResponse
from django.http import HttpResponseRedirect
from .forms import UserForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import  login_required
from django.shortcuts import redirect

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
    replies = Replies.objects.filter(comment_id__in=comments)
    for comment in comments:
        words=comment.text.split()
        comment.text=""
        for comm_word in words:
            if comm_word in forbiddenWords:
                comm_word='*'*len(comm_word)
            comment.text+=" "+comm_word
    for reply in replies:
        words= reply.text.split()
        reply.text=""
        for replyWord in words:
            if replyWord in forbiddenWords:
                replyWord='*'*len(replyWord)
            reply.text+=" "+replyWord
    context={'post':pst,'category':ctg.category_name,'tags':Alltags,'comments':comments,'replies':replies}
    return render(request, 'post.html',context)

def comment(request):
    comm = request.GET.get('comment', None)
    userFk=request.GET.get('user',None)
    userObj=User.objects.get(id=userFk)
    postFk=request.GET.get('post',None)
    pstObj=Posts.objects.get(id=postFk)
    cObj=Comments(user=userObj, post=pstObj, text=comm)
    cObj.save()
    return JsonResponse({'foo': 'bar'})


def reply(request):
    comm = request.GET.get('comment', None)
    userFK = request.GET.get('user', None)
    userObj= User.objects.get(id=userFK)
    commentFK= request.GET.get('comId', None)
    post_id= request.GET.get('postId', None)
    commentObj= Comments.objects.get(id=commentFK)
    comment_replies=commentObj.num_of_replies
    if comment_replies == 0:
        Comments.objects.filter(id=commentFK).update(num_of_replies=1)
        replyObj=Replies(user=userObj , comment=commentObj , text =comm)
        replyObj.save()

    return JsonResponse({'foo': 'bar'})
