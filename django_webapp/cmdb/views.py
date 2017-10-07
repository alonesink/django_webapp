from django.shortcuts import render
from cmdb import models
# Create your views here.

user_list = [
    {"user":"jack","pwd":"abc"},
    {"user":"tom","pwd":"ABC"}
]

def index(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        global user_list
        # 将数据保存在数据库
        models.UserInfo.objects.create(user = username,pwd = password)

        # 从数据库中数据
        user_list = models.UserInfo.objects.all()

        print(username,password)
    return render(request,"index.html",{"data":user_list},None,200)