from django.shortcuts import render

# Create your views here.
def login(request):
    # return HttpResponse('登录')
    return render(request,'users/login.html')