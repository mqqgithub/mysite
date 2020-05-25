from django.urls import path
from cmdb import views

urlpatterns = [
    path(r'index/', views.index)
]
