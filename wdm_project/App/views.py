from django.shortcuts import render

# Create your views here.
def base(request):
    #获取sesson
    return render(request,'base1.html')


def index(request):

    return render(request, 'index.html')


def nav_br1(request):
    return render(request,'nav_br1.html')


def nav_br2(request):
    return render(request,'nav_br2.html')

def nav_br3(request):
    return render(request,'nav_br3.html')

def nav_br4(request):
    return render(request,'nav_br4.html')


def nav_br5(request):
    return render(request,'nav_br5.html')

def nav_br6(request):
    return render(request,'nav_br6.html')

def nav_br7(request):
    return render(request,'nav_br7.html')