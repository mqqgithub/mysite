from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'cmdb/index.html', {'hello': '这里是我的博客', })
def web(request):
    return HttpResponse("hello world")



