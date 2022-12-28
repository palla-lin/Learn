from django.shortcuts import render,HttpResponse,redirect
from blog import models
import sys
sys.path.append('F:\\mappingknowledge\\finance')
from QA_main import ans
import time
# Create your views here.
def login_state_check(fun):
    def inner(request):
        username = request.COOKIES.get('username')

        if username:
            ret=fun(request)
            return ret
        else:
            return render(request,'admin_blog/login.html')

    return inner
def login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        label=request.POST.get('label')
        num=models.user.objects.filter(username=username, password=password).count()
        if num>0:
        # if username=='root' and password=='root':
            rep=redirect( '/manage/chat.html')
        #     rep=render(request,'admin_blog/chat.html')
            rep.set_cookie('username',username)
            return rep
        else:
            return  render(request,'admin_blog/login.html')

    return  render(request,'admin_blog/login.html')
@login_state_check
def ad_index(request):
    return render(request,'admin_blog/index.html')


def blog_index(request):

    re=models.article.objects.values('title','content','time','user_id__username')
    for i in re:
        i['time']=i['time'].strftime('%b %d %Y ')
        i['user']=i['user_id__username']
        del i['user_id__username']
    # return HttpResponse(re)
    return render(request, 'blog/index.html',{'info':re})


def chat(req):
    return render(req,'chat/index.html',{'answer':'成功了111111111111'})
def ajax_post(request):
    question=request.POST.get('new')
    print(question)
    res=ans.get_ans(question)
    return HttpResponse(res)
def code_library(request):
    pass
def post(request):
    pass
def contact(request):
    pass
def about(request):#介绍自己
    pass

def show_demo(req):
    return render(req,'blog/demo.html')
