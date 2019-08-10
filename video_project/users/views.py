from django.contrib.auth import authenticate,login as auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from users.forms import UserLoginForm


def users(request):
    return HttpResponse('用户首页')



def login(request):
    if request.method=='POST':
        next=request.POST.get('next','/')
        form=UserLoginForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                #return redirect('home')
                return redirect(next)
        else:
            print(form.errors)
    else:
        next=request.GET.get('next','/')
        form=UserLoginForm()
    print(next)

    return render(request,'registration/login.html',{'form':form,'next':next})


def signup(request):
    return HttpResponse("注册页面")


def logout(request):
    return HttpResponse("退出登录")