from django.urls import path, re_path
from blog import views

urlpatterns = [
    path(r'index/', views.index),
    # django2.x 之后用正则表达式，必须引用re_path函数
    re_path(r'article/(?P<article_id>[0-9]+)', views.article_page, name='article_page'),
    re_path(r'edit/(?P<article_id>[0-9]+)', views.edit_page, name='edit_page'),
    path(r'edit_action/', views.edit_action, name='edit_action')
]
