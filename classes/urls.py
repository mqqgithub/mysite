from django.urls import path, re_path
from classes import views

urlpatterns = [
    # path(r'index/', views.index),
    # django2.x 之后用正则表达式，必须引用re_path函数
    # re_path(r'article/(?P<article_id>[0-9]+), views.article_page, name='article_page'),
    # re_path(r'^index$', views.index),  # 访问地址中不要在加上‘/’,会自动加上
    re_path(r'^index$', views.index, name='index'),  # 伪静态
    re_path(r'^login$', views.login, name='login'),
]