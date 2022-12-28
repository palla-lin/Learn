from django.shortcuts import render,redirect,HttpResponse
from users_management import models
# Create your views here.

def tr(req):

    print(req)
    return HttpResponse('123456789')


def login (request):
    ms=''
    if request.method=='POST':
        user=request.POST.get('user')
        pwd=request.POST.get('pwd')
        if user=='root' and pwd=='root':
            rep=redirect('index.html')
            rep.set_cookie('username',user,)
            return rep
        else:
            ms='用户名错误'
    return render(request,'login.html',{'ms':ms})

def index(request):

    username=request.COOKIES.get('username')
    if username:
        username='lpl'
        return render(request, 'index.html',{'username':username})
    else:
        return redirect('login.html')

def bootstrap(req):
    return render(req,'bootstrap.html')