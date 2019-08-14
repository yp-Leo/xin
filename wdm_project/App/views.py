from django.shortcuts import render

# Create your views here.
def index(request):
    username = request.COOKIES.get('username')
    return render(request,'index.html',context={'username':username})


def nav_br1(request):
    username = request.COOKIES.get('username')
    return render(request,'nav_br1.html',context={'username':username})


def nav_br2(request):
    username = request.COOKIES.get('username')
    return render(request,'nav_br2.html',context={'username':username})


def nav_br3(request):
    username = request.COOKIES.get('username')
    return render(request,'nav_br3.html',context={'username':username})


def nav_br4(request):
    username = request.COOKIES.get('username')
    return render(request,'nav_br4.html',context={'username':username})


def nav_br5(request):
    username = request.COOKIES.get('username')
    return render(request,'nav_br'+'5'+'.html',context={'username':username})


def nav_br6(request):
    username = request.COOKIES.get('username')
    return render(request,'nav_br6.html',context={'username':username})


def nav_br7(request):
    username = request.COOKIES.get('username')
    return render(request,'nav_br7.html',context={'username':username})


