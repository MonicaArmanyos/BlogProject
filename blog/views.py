from django.shortcuts import render
from .models import Categories, Posts ,Tags ,CategoryUser ,Comments,Replies,ForbiddenWords,Likes
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UserForm
from django.contrib.auth import authenticate , login , logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import  login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers


def homepage(request):
    subcat= sub(request)
    allPosts = Posts.objects.all().order_by("-created_at")
    paginator = Paginator(allPosts, 5)
    page = request.GET.get('page')
    try:
        posts= paginator.page(page)
    except PageNotAnInteger:
        posts= paginator.page(1)
    except EmptyPage:
        posts= paginator.page(paginator.num_pages)
    context = {'allCategories':Categories.objects.all(), 'allPosts':posts, "subcat": subcat}
    return render(request, 'homepage/homepage.html', context)


def search(request):
    found_posts = Posts.objects.filter(title__icontains=request.GET['term'])
    try:
        tag=Tags.objects.get(tag_name__contains=request.GET['term'])
        found_postt=Posts.objects.filter(tag=tag.id)
    except:
        return render(request, "homepage/search.html",{'allPosts':found_posts,'allCategories':Categories.objects.all()})
    else:
        return render(request, "homepage/search.html",{'allPosts':found_postt,'allCategories':Categories.objects.all()})


def getCategoryPosts(request, cat_id):
    get_category = Categories.objects.get(id=cat_id)
    context = {'allPosts':Posts.objects.filter(category_id=get_category.id).order_by('-created_at')}
    return render(request, "homepage/homepage.html", context)


def subscribe (request):
    cat_id=request.GET.get('catid',None)
    user_id=request.user.id
    sub=CategoryUser.objects.create(category_id=cat_id ,user_id=user_id)
    sub.save()
    responseData = {
        'json': True
    }

    return JsonResponse(responseData,safe=False)


def unsubscribe (request):
    cat_id=request.GET.get('catid',None)
    user_id=request.user.id
    unsub=CategoryUser.objects.get(category_id=cat_id ,user_id=user_id)
    unsub.delete()
    responseData = {
        'json': True
    }


def sub(request):
    catsub=Categories.objects.filter(user=request.user.id)
    cat_sub=[]
    for i in catsub:
        cat_sub.append(i.id)
    return cat_sub

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



    return JsonResponse({'foo': 'bar'})

