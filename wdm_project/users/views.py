import hashlib

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from users.models import User
from wdm_project.settings import MAXAGE




def login(request):
    if request.method == 'POST':
        # 1 获取数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        # 2 验证
        if User.check_login(username, password):
            # 3 写session信息
            print('1',username,password)
            response = redirect(reverse("App:index"))
            # session
            request.session['username'] = username
            # 设置过期时间
            request.session.set_expiry(MAXAGE)
            return response
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')

def logout(request):
    response = redirect(reverse('App:index'))
    #session
    #清空session并删除表中数据
    request.session.flush()
    return response


# def add(request):
#     user = User(username='admin',password_hash=hashlib.sha1(b'123456').hexdigest(),mobile='13520335341',email='1615910073@qq.com')
#     user.save()
#
#     return HttpResponse('添加成功')