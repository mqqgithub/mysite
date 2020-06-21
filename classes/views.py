from django.shortcuts import render , HttpResponse, redirect
import datetime
from classes.models import UserInfo


# Create your views here.
def index(request, name):
    # now = datetime.datetime.now()
    # return HttpResponse(now)
    # UserInfo.objects.filter(nid=1, username='admin')
    # UserInfo.objects.filter(nid__gt=1)   nid>1
    # UserInfo.objects.filter(nid__lt=1)   nid<1
    # UserInfo.objects.filter(nid=1, username='admin').delete()
    # UserInfo.objects.filter(nid=1, username='admin').update(username='admin11')
    # UserInfo.objects.all()
    # UserInfo.objects.create(username='', password='')
    # UserInfo.objects.get(id=123)
    print('name', name)
    return render(request, 'index.html', {'msg': '请登录！', 'user': '陌生人'})


def login(request):
    if request.method == 'GET':
        # namelist = []
        # userlist = UserInfo.objects.get
        # for u in userlist:
        #     namelist.append(u.)
        # print(namelist)
        return render(request, 'login.html', {'msg': '请登录！', 'user': ['1', '2']})
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')

        pwd = UserInfo.objects.get(username=u).password
        print(pwd)
        if p == pwd:
            # return redirect('https://www.tmall.com/')
            # return redirect('/classes/index')
            return render(request, 'index.html', {'msg': '登录成功！', 'user': u})
        else:
            return render(request, 'index.html', {'msg': '登录失败！'})


def user(request):

    if request.method == 'GET':
        users = UserInfo.objects.all()
        return render(request, 'user.html', {'users': users})


def del_user(request):
    user_id = request.GET.get('nid')
    UserInfo.objects.filter(nid=user_id).delete()
    return redirect('/classes/user')


def add_user(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        UserInfo.objects.create(username=user, password=pwd)
        return redirect('/classes/user')
    if request.method == 'GET':
        return render(request, 'add_user.html')


def edit_user(request):
    if request.method == 'GET':
        user_id = request.GET.get('nid')
        user_name = UserInfo.objects.filter(nid=user_id).values('username')[0]['username']
        password = UserInfo.objects.filter(nid=user_id).values('password')[0]['password']
        return render(request, 'edit_user.html', {"nid": user_id, "username": user_name, 'password': password})
    if request.method == 'POST':
        user_id = request.POST.get("nid")
        user_name = request.POST.get("username")
        print(user_name)
        password = request.POST.get("password")
        UserInfo.objects.filter(nid=user_id).update(username=user_name, password=password)
        return redirect('/classes/user')



