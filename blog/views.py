from django.shortcuts import render
from .models import Categories, Posts ,Tags ,CategoryUser ,Comments,Replies,ForbiddenWords,Likes
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import RegUserForm
from django.contrib.auth import authenticate , login , logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import  login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def sub(request):
    catsub = Categories.objects.filter(user=request.user.id)
    cat_sub = []
    for i in catsub:
        cat_sub.append(i.id)
    return cat_sub


def homepage(request):
    subcat = sub(request)
    allPosts = Posts.objects.all().order_by("-created_at")
    paginator = Paginator(allPosts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'allCategories': Categories.objects.all(), 'allPosts': posts, "subcat": subcat}
    return render(request, 'homepage/homepage.html', context)


def search(request):
    found_posts = Posts.objects.filter(title__icontains=request.GET['term']).order_by('-created_at')
    try:
        tag = Tags.objects.get(tag_name__contains=request.GET['term'])
        found_postt = Posts.objects.filter(tag=tag.id)
    except:
        return render(request, "homepage/search.html", {'allPosts': found_posts, 'allCategories': Categories.objects.all()})
    else:
        return render(request, "homepage/search.html", {'allPosts': found_postt, 'allCategories': Categories.objects.all()})


def getCategoryPosts(request, cat_id):
    subcat = sub(request)
    get_category = Categories.objects.get(id=cat_id)
    context = {'allPosts': Posts.objects.filter(category_id=get_category.id).order_by('-created_at'),'allCategories': Categories.objects.all() , "subcat": subcat}
    return render(request, "homepage/homepage.html", context)


def subscribe(request):
    cat_id = request.GET.get('catid', None)
    category = Categories.objects.get(id=cat_id)
    user_id = request.user.id
    sub = CategoryUser.objects.create(category_id=cat_id, user_id=user_id)
    sub.save()
    subject = 'Thanks For Checking The Blog'
    message = 'You have Subscribed To a New Category Which is : ' + str(category.category_name)
    from_email = settings.EMAIL_HOST_USER
    to_list = [request.user.email]
    send_mail(subject, message, from_email, to_list, fail_silently=True)

    responseData = {
        'json': True
    }

    return JsonResponse(responseData, safe=False)


def unsubscribe(request):
    cat_id = request.GET.get('catid', None)
    user_id = request.user.id
    unsub = CategoryUser.objects.get(category_id=cat_id, user_id=user_id)
    unsub.delete()
    responseData = {
        'json': True
    }

    return JsonResponse(responseData, safe=False)


def post(request,post_id):
    isliked = 0
    isdisliked = 0
    try:
        pst=Posts.objects.get(id=post_id)
    except:
        return HttpResponseRedirect('/blog/postNotFound')





    if request.user.is_authenticated():
        record = Likes.objects.all().filter(state=1, user=request.user, post=pst)
        record1 = Likes.objects.all().filter(state=0, user=request.user, post=pst)
        if record.exists():
            isliked = 1
        if record1.exists():
            isdisliked = 1


    countlikes = Likes.objects.all().filter(state=1, post=pst).count()
    countdislike = Likes.objects.all().filter(state=0, post=pst).count()



    ctg=Categories.objects.get(id=pst.category_id)

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
    context={'post':pst,'category':ctg.category_name,'comments':comments,'replies':replies,"plikes":countlikes ,"pdislike":countdislike ,"userlike":isliked,"userdislike":isdisliked}
    return render(request, 'post.html',context)

def comment(request):
    comm = request.GET.get('comment', None)
    userFk=request.GET.get('user',None)
    userObj=User.objects.get(id=userFk)
    postFk=request.GET.get('post',None)
    pstObj=Posts.objects.get(id=postFk)
    cObj=Comments(user=userObj, post=pstObj, text=comm)
    cObj.save()

    lastComment=Comments.objects.filter().order_by('-id')[0]

    forbiddenWords=[]
    Rej_words=ForbiddenWords.objects.all()
    for word in Rej_words:
        forbiddenWords.append(word.word)
    words=lastComment.text.split()
    lastComment.text=""
    for comm_word in words:
        if comm_word in forbiddenWords:
            comm_word='*'*len(comm_word)
        lastComment.text+=" "+comm_word

    commentJson={'commentText':lastComment.text,'commentId':lastComment.id}
    return JsonResponse(commentJson,safe=False)


def reply(request):
    comm = request.GET.get('comment', None)
    userFK = request.GET.get('user', None)
    userObj= User.objects.get(id=userFK)
    commentFK= request.GET.get('comId', None)
    post_id= request.GET.get('postId', None)
    commentObj= Comments.objects.get(id=commentFK)
    comment_replies=commentObj.num_of_replies

    Comments.objects.filter(id=commentFK).update(num_of_replies=1)
    replyObj=Replies(user=userObj , comment=commentObj , text =comm)
    replyObj.save()

    lastReply=Replies.objects.filter().order_by('-id')[0]

    forbiddenWords=[]
    Rej_words=ForbiddenWords.objects.all()
    for word in Rej_words:
        forbiddenWords.append(word.word)
    words=lastReply.text.split()
    lastReply.text=""
    for comm_word in words:
        if comm_word in forbiddenWords:
            comm_word='*'*len(comm_word)
        lastReply.text+=" "+comm_word

    replyJson={'replyText':lastReply.text,'replyId':lastReply.id}
    return JsonResponse(replyJson,safe=False)

def makelike(request,post_id):
    if request.user.is_authenticated():
        post = Posts.objects.filter(id=post_id)

        record=Likes.objects.all().filter(state=1, user=request.user, post=post[0])
        record2=Likes.objects.all().filter(state=0, user=request.user, post=post[0])
        if record.exists():
            deletelike=Likes.objects.get(state=1, user=request.user, post=post[0])
            deletelike.delete()
        else:
            Likes.objects.create(state=1, user=request.user, post=post[0])


        if record2.exists():
            deletelike=Likes.objects.get(state=0, user=request.user, post=post[0])
            deletelike.delete()










    return HttpResponse("data")


def makedislike(request,post_id):
    if request.user.is_authenticated():
        post = Posts.objects.filter(id=post_id)
        pst = Posts.objects.get(id=post_id)

        record=Likes.objects.all().filter(state=0, user=request.user, post=post[0])
        record2 = Likes.objects.all().filter(state=1, user=request.user, post=post[0])

        if record.exists():
            deletelike=Likes.objects.get(state=0, user=request.user, post=post[0])
            deletelike.delete()
        else:
            Likes.objects.create(state=0, user=request.user, post=post[0])

        if record2.exists():
            deletelike = Likes.objects.get(state=1, user=request.user, post=post[0])
            deletelike.delete()

        postdel = Likes.objects.filter(state=0, post=pst).count()
        if postdel >= 10:
            pst.delete()
            responseData = {
                'json': True,
                'del' :1
            }

            return JsonResponse(responseData, safe=False)









    return JsonResponse({'foo': 'bar'})







def postNotFound(request):
    return render(request, 'homepage/postnotfound.html')







def index(request):
    return  render(request,"homepage.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse("You Are Logged In")


def register(request):
    usr_form=RegUserForm()

    if request.method=="POST":
        users = User.objects.all().filter(email=request.POST['email'])
        if users.exists():
            return render(request, "login&&register/registeration.html", {"form": usr_form, "dublemail": 1})
        usr_form = RegUserForm(request.POST)
        if usr_form.is_valid():
            usr_form.save()
            return HttpResponseRedirect("/blog/login")
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























