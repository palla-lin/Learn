from django.shortcuts import render,HttpResponse
from blog import models
# Create your views here.
user_list=[]
def userInfo(req):#req为前端信息
    print('8888')
    if req.method=="POST":
        u=req.POST.get('username',None)
        s = req.POST.get('sex', None)
        e = req.POST.get('email', None)
        # user = {"username": username, "sex": sex, "email": email}
        # user_list.append(user)
        # print(user_list)
        models.UserInfo.objects.create(
            username=u,
            sex=s,
            email=e,
        )
        user_list=models.UserInfo.objects.all()
    else:
        user_list =[]
    return render(req,'user.html',{'user_list':user_list})

# ,{'user_list':user_list}
