# -*- coding:utf-8 -*-
# @Time : 2021/11/26 22:23
# @Author : Sakura
# @QQEmail : 1018655370@qq.com
# @Google : jiangjiefeng0@gmail.com
from django.conf.urls import url
from . import views
urlpatterns = [
    url("^students/$", views.Student.as_view()),
    url("^classrooms/$", views.Classroom.as_view()),
    url("^coursera/$", views.Coursera.as_view()),
    url("^headers/(?P<pk>\d+)", views.Headers.as_view()),
    url("^deletemanager/", views.ManagerDelete.as_view()),
    url("^courseramanager/", views.CouseraManager.as_view()),
    url("^ManagerSorting/", views.ManagerSorting.as_view())
]