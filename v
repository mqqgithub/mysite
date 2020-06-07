from django.shortcuts import render, HttpResponse
def fun(request):
    # 返回字符串
    return HttpResponse('str')

def func(request):
    # 自动到setting中设置的路径寻找文件，读取内容并返回给用户，本质是调用HttpPResponse
    return render(request, 'login.html')

def fun(request):
    pass
