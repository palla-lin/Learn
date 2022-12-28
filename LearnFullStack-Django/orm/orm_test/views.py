from django.shortcuts import render,HttpResponse
from orm_test import models
# Create your views here.
# 字段默认不为空，Null=True
#插入数值，create有两种方式，一种键值对，一种字典加**{}
#插入数值，author=Author()
# author.save()
#queryset 可迭代 可切片 惰性
def orm_test(request):
    # -----------------------查询---------------------------------
    # re=models.Book.objects.filter().order_by('price').values()
    # re=models.Book.objects.values().filter(id=1)
    # re = models.Book.objects.filter(id__lt=3,id__gt=1).values('title')2
    # re = models.Book.objects.filter(id__in=[1,2]).values('title'),1,2
    # re=models.Book.objects.get(id=0)
    # re = models.Book.objects.filter(id__range=[1,3]).values('title')1,2,3
    # re1=models.Book.objects.all()
    # re=models.Book.objects.values('title','color')
    # re=models.Book.objects.filter(price=48).values()
    # re = models.Book.objects.filter(publisher__city='广东').values()
    # re = models.Book.objects.filter(author__name='毛泽东').values()
    # print(re,type(re),'123',re[0],type(re[0]))'
    # models.Book.objects.filter(title='漂流记').update()
    # -------------------------------------------------------
    # print(re,type(re))
    # return render(request,'orm.html',{'result':re,'label':'2211'})
    print(request.POST)
    print(request.GET)
    print(request.FILES)
    return render(request,'html_test.html')
def orm_add(req):
    models.Book.objects.create(
        title='漂流记',
        price=1,
        color='yellow',
        publisher_id=4
    )
    return HttpResponse('ok')



#改update方法是queryset对象方法，get返回一个model对象，save会更新一行所有列
def orm_update1():
    author=models.Author.objects.get(name='')
    author.name=''
    author.save()
def orm_update2():
    models.Book.objects.filter().update()

#判断存不存在
def e():
    models.Book.objects.exists()
#多表创建------------------------------
# 一对多，外键在多的里面
#插值时，默认创建字段名_id
#多对多
# models.manytomanyField()或者使用两次一对多，联合唯一主键
# authorl=models.Author.objects.get（id=3）author2=models.Author.objects.get（id=4）
# book=mode1s.Book.objects.filter（id=3）[0]
# #book绑定的作者对象集合
# book.author.add（author1，author2）I