import hashlib

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.


# 登录函数
from django.urls import reverse

from App.models import User
from users.forms import UserForm
from wdm_project.settings import MAXAGE


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid() and User.isexist(form.cleaned_data['username']):
            # create_user
            del form.cleaned_data['confirm_password']
            print(form.cleaned_data)
            # form.cleaned_data['is_active'] = False
            password=request.POST.get('password_hash')
            form.cleaned_data['password_hash']=hashlib.sha1(password.encode('utf8')).hexdigest()
            # form.cleaned_data['password_hash']=request.POST.get('password_hash')
            User.objects.create(**form.cleaned_data)

            # 注册后自动登录
            request.session['username'] = form.cleaned_data['username']
            # 设置过期时间
            request.session.set_expiry(MAXAGE)
            return redirect(reverse('App:nav_br5'))
        return render(request, 'register.html', {'form': form})
    form = UserForm()
    return render(request, 'register.html', {'form': form})



def login(request):
    # 记录第一次进来的时候，上次访问的地址，（以便于访问后，调回到原来的地址）
    if request.method == 'GET':
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')

    elif request.method == 'POST':
        #1 获取数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        password = hashlib.sha1(password.encode('utf8')).hexdigest()

        # 登录验证码
        # mCode = request.POST.get('mCode')

        #2 验证
        if User.check_login1(username,password):
            response = redirect(request.session['login_from'])

            #3 写session
            request.session['username'] = username
            #设置过期时间
            request.session.set_expiry(MAXAGE)
            return response
        elif User.check_login2(username,password):
            response = redirect(request.session['login_from'])

            # 过滤出邮箱对应的用户名，以便在头上显示用户名
            username_real = list(User.objects.filter(email=username,password_hash=password).values('username'))
            request.session['username'] = username_real[0]['username']
            # 设置过期时间
            request.session.set_expiry(MAXAGE)
            return response
    return render(request,'login.html')

#退出
def logout(request):
    response = redirect(reverse('App:index'))
    response.delete_cookie('username')

    #session
    #清空session并删除表中数据
    request.session.flush()
    return response


# def logout(request):
#     HttpResponse.delete_cookie('username', path='/', domain=None)
#     # return render(request,'index.html')
#     return redirect(reverse('App:index'))
#     # return HttpResponse("退出")
#
# 注册函数
# def register(request):
#     # return HttpResponse('注册')
#     if request.method == 'POST':
#         return HttpResponse("注册")
#     return render(request,'register.html')

