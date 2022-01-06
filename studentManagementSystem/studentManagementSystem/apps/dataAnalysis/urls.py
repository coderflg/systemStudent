# -*- coding:utf-8 -*-
# @Time : 2021/11/30 18:15
# @Author : Sakura
# @QQEmail : 1018655370@qq.com
# @Google : jiangjiefeng0@gmail.com
from django.conf.urls import url
from . import views
urlpatterns = [
    url("^analysis/$", views.StudentAnalysis.as_view())
]