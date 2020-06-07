"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import HttpResponse


def default(request):
    return HttpResponse('默认页面')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', views.index)
    path(r'cmdb/', include('cmdb.urls')),
    # 注意写法和1.0不同
    path(r'blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path(r'classes/', include(('classes.urls', 'classes'), namespace='classes')),
    re_path(r'^', default),  # 没有路由到，返回默认页面
]
