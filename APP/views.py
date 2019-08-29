from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 登录
def login(request):
    # data = []
    return render(request, "login/login.html")
    # return HttpResponse('1111111111111111')


